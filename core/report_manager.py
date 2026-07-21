# AR-GhostNet | The Archivist
# Location: core/report_manager.py

import os
from datetime import datetime
from utils.colors import Colors

class ReportManager:
    def __init__(self):
        self.report_dir = "reports"
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

    def save_report(self, target, module_name, data):
        """
        Saves the scan results into a target-specific file.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{self.report_dir}/report_{target.replace('.', '_')}.txt"
        
        try:
            with open(filename, "a") as f:
                f.write(f"\n{'-'*50}\n")
                f.write(f"Module: {module_name}\n")
                f.write(f"Timestamp: {timestamp}\n")
                f.write(f"{'-'*50}\n")
                f.write(data)
                f.write("\n")
            return f"Report saved to {filename}"
        except Exception as e:
            return f"Error saving report: {str(e)}"

    def get_all_reports(self):
        return os.listdir(self.report_dir)