"""
🧠 MEMORY ENGINE - Vector + Graph Hybrid
Stores and retrieves your cognitive history
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any
import chromadb
from chromadb.config import Settings
import networkx as nx


class CognitiveMemory:
    """Hybrid memory system: vector for semantic search, graph for relationships"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        
        # Vector memory for semantic search
        self.chroma_client = chromadb.Client(Settings(
            anonymized_telemetry=False,
            allow_reset=True
        ))
        
        try:
            self.collection = self.chroma_client.get_collection("cognitive_memory")
        except:
            self.collection = self.chroma_client.create_collection("cognitive_memory")
        
        # Knowledge graph for concept relationships
        self.graph = nx.DiGraph()
        self._load_graph()
    
    def add_memory(self, content: str, memory_type: str, metadata: Dict = None):
        """Store a memory with semantic embedding"""
        memory_id = f"{memory_type}_{datetime.now().timestamp()}"
        
        meta = {
            "type": memory_type,
            "timestamp": datetime.now().isoformat(),
            **(metadata or {})
        }
        
        self.collection.add(
            documents=[content],
            metadatas=[meta],
            ids=[memory_id]
        )
        
        return memory_id
    
    def search_memories(self, query: str, n_results: int = 5, memory_type: str = None):
        """Semantic search through memories"""
        where = {"type": memory_type} if memory_type else None
        
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where
        )
        
        return results
    
    def add_concept_link(self, concept_a: str, concept_b: str, relationship: str):
        """Add relationship between concepts in knowledge graph"""
        self.graph.add_edge(concept_a, concept_b, relationship=relationship)
        self._save_graph()
    
    def get_related_concepts(self, concept: str, depth: int = 2):
        """Get concepts related to a given concept"""
        if concept not in self.graph:
            return []
        
        related = []
        for node in nx.single_source_shortest_path_length(self.graph, concept, cutoff=depth):
            if node != concept:
                related.append(node)
        
        return related
    
    def _load_graph(self):
        """Load knowledge graph from disk"""
        graph_path = os.path.join(self.data_dir, "knowledge_graph.json")
        if os.path.exists(graph_path):
            with open(graph_path, 'r') as f:
                data = json.load(f)
                self.graph = nx.node_link_graph(data)
    
    def _save_graph(self):
        """Save knowledge graph to disk"""
        graph_path = os.path.join(self.data_dir, "knowledge_graph.json")
        data = nx.node_link_data(self.graph)
        with open(graph_path, 'w') as f:
            json.dump(data, f, indent=2)
