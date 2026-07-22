
tickets = [
    {"status": "open", "priority": "high", "channel": "email"},
    {"status": "closed", "priority": "low", "channel": "phone"},
    {"status": "in_progress", "priority": "medium", "channel": "chat"},
    {"status": "open", "priority": "high", "channel": "email"},
]

class ServiceMetrics:
    def __init__(self, tickets: list):
        self.tickets = tickets
        
    def get_metrics() -> dict:
        total = len(tickets)
        by_status = {}
        by_priority = {}
        by_channel = {}

        for ticket in tickets:
            status = ticket.get("status")
            priority = ticket.get("priority")
            channel = ticket.get("channel")

            if status:
                by_status[status] = by_status.get(status, 0) + 1
            if priority:
                by_priority[priority] = by_priority.get(priority, 0) + 1
            if channel:
                by_channel[channel] = by_channel.get(channel, 0) + 1

        return {
            "total": total,
            "by_status": by_status,
            "by_priority": by_priority,
            "by_channel": by_channel,
        }