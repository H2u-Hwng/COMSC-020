def to_minutes(obj):
    return obj.hour * 60 + obj.minute

def from_military(s):
    """Create Clock object from military-format time string"""
    s = s.strip()
    hr = int(s[0:2])
    minute = int(s[2:4])
    return Clock(hr, minute)

def from_am_pm(s):
    """Create Clock object from string in form hh:mm AM/PM"""
    s = s.strip()
    [h, m] = s.split(':')
    hour = int(h) % 12
    minute = int(m[0:2]) % 60
    suffix = m[2:]
    suffix = suffix.strip().upper()
    if suffix[0] == 'P':
       hour = hour + 12
    return Clock(hour, minute)

class Clock:

    def __init__(self, hour, minute):
        self.hour = abs(hour) % 24
        self.minute = abs(minute) % 60
    
    def __str__(self):
        return format(self.hour, '02d') + format(self.minute, '02d')
    
    def add(self, other):
        self_min = to_minutes(self)
        other_min = to_minutes(other)
        total = self_min + other_min
        return Clock(total // 60, total % 60)
    
    def subtract(self, other):
        self_min = to_minutes(self)
        other_min = to_minutes(other)
        result = max(self_min, other_min) - min(self_min, other_min)
        return Clock(result // 60, result % 60)
    
