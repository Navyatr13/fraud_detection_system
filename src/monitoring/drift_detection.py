from evidently import ColumnDriftMetric
from evidently.report import Report

def detect_drift(data):
    report = Report(metrics=[ColumnDriftMetric()])
    report.run(reference_data=data["reference"], current_data=data["current"])
    return report
