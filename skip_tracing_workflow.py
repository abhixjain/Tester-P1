class SkipTracingWorkflow:
    def __init__(self):
        # Possible stages
        self.stages = []
        # Task groups for accounts in validation stage
        self.validation_task_groups = {}

    def add_needs_skip_tracing(self, account_id):
        if "Needs Skip Tracing" not in self.stages:
            self.stages.append("Needs Skip Tracing")
            print(f"[INFO] 'Needs Skip Tracing' stage added for account {account_id}.")

    def automated_skip_trace_in_progress(self, account_id, from_cbc=False):
        if from_cbc or "Needs Skip Tracing" in self.stages:
            if "Needs Skip Tracing" in self.stages:
                self.stages.remove("Needs Skip Tracing")
            if "Skip Trace in Progress" not in self.stages:
                self.stages.append("Skip Trace in Progress")
                print(f"[AUTO] 'Skip Trace in Progress' stage set for account {account_id}.")

    def automated_skip_trace_validation(self, account_id, from_cbc=False):
        if from_cbc or "Skip Trace in Progress" in self.stages:
            if "Skip Trace in Progress" in self.stages:
                self.stages.remove("Skip Trace in Progress")
            if "Skip Trace Validation" not in self.stages:
                self.stages.append("Skip Trace Validation")
                print(f"[AUTO] 'Skip Trace Validation' stage set for account {account_id}.")
            # Assign to a task group
            self.validation_task_groups[account_id] = "default_task_group"

    def manually_remove_validation_stage(self, account_id):
        if "Skip Trace Validation" in self.stages:
            self.stages.remove("Skip Trace Validation")
            self.validation_task_groups.pop(account_id, None)
            print(f"[MANUAL] 'Skip Trace Validation' removed for account {account_id}.")

    def get_current_stage(self):
        return self.stages

# Example usage
workflow = SkipTracingWorkflow()
account_id = "ACC12345"
workflow.add_needs_skip_tracing(account_id)  # Manual
workflow.automated_skip_trace_in_progress(account_id, from_cbc=True)  # Automated
workflow.automated_skip_trace_validation(account_id, from_cbc=True)  # Automated
workflow.manually_remove_validation_stage(account_id)  # Manual
