# Multi-Agent AI System for Self-Healing Test Automation

## Overview
This project implements a multi-agent system to automatically detect, diagnose, and fix test automation failures using AI, knowledge graphs, and LLMs.

## Agents
- **Finder**: Identifies test failures from logs/reports.
- **Detector**: Locates failure points and checks dependencies.
- **Investigator**: Analyzes root cause.
- **Solution Provider**: Suggests fixes using LLM + RAG.
- **Solution Applier**: Applies fixes to codebase.
- **Solution Tester**: Validates fixes by running tests.
- **Chat Manager**: Orchestrates agent communication and state.

## Core Components
- **Knowledge Graph**: Neo4j for dependency tracking.
- **Global Memory**: ChromaDB for agent communication.
- **State Management**: Centralized, managed by Chat Manager.

## Workflow
1. Convert repo to knowledge graph.
2. Finder detects failures.
3. Detector/Investigator analyze root cause.
4. Solution Provider generates fix.
5. Solution Applier implements fix.
6. Solution Tester validates.
7. If failure persists, loop back.

## Requirements
See `requirements.txt` for dependencies.
