
class Utility:
    def convertSecondstoHoursMinutesSeconds(self,total_seconds):
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        total_seconds %= 60
        print(f"{hours}:{minutes}:{total_seconds}")
        return f"{hours}:{minutes}:{total_seconds}"

