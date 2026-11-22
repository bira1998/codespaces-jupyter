from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import sys

scheduler = BlockingScheduler(timezone="Asia/Kolkata")

def run_agent():
    print("\nStarting AI Agent...")
    subprocess.run([sys.executable, "agent.py"])

scheduler.add_job(run_agent, "cron", day_of_week="mon", hour=9, minute=0)

print("AI Agent Scheduler Started!")
print("Agent will run every Monday at 9:00 AM IST")

scheduler.start()