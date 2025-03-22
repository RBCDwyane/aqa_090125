import unittest
from homework_16 import TeamLead
class TestTeamLead(unittest.TestCase):
    def test_team_lead_valid_attributes(self):
        team_lead = TeamLead("Edward", 4100, "QA_Automation", "Python", 4)

        self.assertEqual(team_lead.name, "Edward")
        self.assertEqual(team_lead.salary, 4100)
        self.assertEqual(team_lead.department, "QA_Automation")
        self.assertEqual(team_lead.programming_language, "Python")
        self.assertEqual(team_lead.team_size, 4)

    def test_team_lead_invalid_name(self):
        with self.assertRaises(TypeError):
            TeamLead(123, 4100, "QA_Automation", "Python", 4)
    def test_team_lead_invalid_salary(self):
        with self.assertRaises(TypeError):
            TeamLead("Edward", "4100", "QA_Automation", "Python", 4)
    def test_team_lead_invalid_department(self):
        with self.assertRaises(TypeError):
            TeamLead("Edward", 4100, 123, "Python", 4)
    def test_team_lead_invalid_programming_language(self):
        with self.assertRaises(TypeError):
            TeamLead("Edward", 4100, "QA_Automation", 123, 4)
    def test_team_lead_invalid_team_size(self):
        with self.assertRaises(TypeError):
            TeamLead("Edward", 4100, "QA_Automation", "Python", "four")


if __name__ == '__main__':
    unittest.main()