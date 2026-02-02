import unittest
import os

class TestMyBatchSystem(unittest.TestCase):
    # 폴더 생성 확인
    def test_folders_exist(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.assertTrue(os.path.exists(os.path.join(BASE_DIR, "input")))
        self.assertTrue(os.path.exists(os.path.join(BASE_DIR, "output")))

    # csv 파일 확인
    def test_report_creation(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        report_path = os.path.join(BASE_DIR, "reports", "final_report.csv")
        # batch_process 실행 여부 확인
        self.assertTrue(os.path.exists(report_path))

if __name__ == '__main__':
    unittest.main()