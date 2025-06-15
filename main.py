from agents.finder import Finder
from agents.detector import Detector
from agents.investigator import Investigator
from agents.solution_provider import SolutionProvider
from agents.solution_applier import SolutionApplier
from agents.solution_tester import SolutionTester
from agents.chat_manager import ChatManager
from core.knowledge_graph import KnowledgeGraph
from core.state_manager import StateManager
from core.memory import Memory

def main():
    # Initialize core components
    kg = KnowledgeGraph()
    state = StateManager()
    memory = Memory()
    chat = ChatManager()
    # Initialize agents
    finder = Finder()
    detector = Detector()
    investigator = Investigator()
    solution_provider = SolutionProvider()
    solution_applier = SolutionApplier()
    solution_tester = SolutionTester()

    # Sample: Read logs from file and run workflow
    with open("sample_logs.txt", "r") as f:
        logs = f.read()
    print("\n===== SAMPLE LOGS =====\n" + logs + "\n=======================\n")
    kg.update_graph("repo_data")
    failures = finder.find_failures(logs)
    print(f"\nDetected Failures: {failures}\n")
    for test_case in failures:
        fail_info = detector.detect_failure_point(test_case, kg="<simulated_graph>", logs=logs)
        print(f"Failure Info for {test_case}: {fail_info}")
        root_cause = investigator.investigate(fail_info)
        print(f"Root Cause for {test_case}: {root_cause}")
        solution = solution_provider.provide_solution({**fail_info, **root_cause})
        print(f"Proposed Solution for {test_case}: {solution}")
        applied = solution_applier.apply_solution(solution, script="<simulated_script>")
        print(f"Solution Applied for {test_case}: {applied}")
        if applied:
            result = solution_tester.test_solution(test_case, results="<simulated_results>")
            print(f"Test Result for {test_case}: {result}")
            state.update_state(test_case, "fixed" if result else "failed")
        else:
            state.update_state(test_case, "apply_failed")
    chat.manage(state.state)
    print("\nMulti-Agent AI System Run Complete.\n")

if __name__ == "__main__":
    main()
