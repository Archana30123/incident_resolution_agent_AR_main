import sys
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))


class CrewConfigTests(unittest.TestCase):
    def test_agent_and_task_configs_are_mappings(self) -> None:
        project_root = Path(__file__).resolve().parents[1]
        agents_path = project_root / 'src' / 'incident_resolution_agent' / 'config' / 'agents.yaml'
        tasks_path = project_root / 'src' / 'incident_resolution_agent' / 'config' / 'tasks.yaml'

        agents_config = yaml.safe_load(agents_path.read_text(encoding='utf-8'))
        tasks_config = yaml.safe_load(tasks_path.read_text(encoding='utf-8'))

        self.assertIsInstance(agents_config, dict)
        self.assertIn('incident_triage_agent', agents_config)
        self.assertIsInstance(agents_config['incident_triage_agent'], dict)
        self.assertIn('log_analysis_agent', agents_config)
        self.assertIsInstance(agents_config['log_analysis_agent'], dict)

        self.assertIsInstance(tasks_config, dict)
        self.assertIn('triage_task', tasks_config)
        self.assertIsInstance(tasks_config['triage_task'], dict)
        self.assertIn('log_analysis_task', tasks_config)
        self.assertIsInstance(tasks_config['log_analysis_task'], dict)

    def test_task_context_dependencies_only_reference_earlier_tasks(self) -> None:
        project_root = Path(__file__).resolve().parents[1]
        tasks_path = project_root / 'src' / 'incident_resolution_agent' / 'config' / 'tasks.yaml'

        tasks_config = yaml.safe_load(tasks_path.read_text(encoding='utf-8'))
        task_order = ['log_analysis_task', 'triage_task']

        for task_name in task_order:
            task_config = tasks_config[task_name]
            context = task_config.get('context', [])
            if not context:
                continue

            current_index = task_order.index(task_name)
            for dependency in context:
                self.assertLess(task_order.index(dependency), current_index)


if __name__ == '__main__':
    unittest.main()
