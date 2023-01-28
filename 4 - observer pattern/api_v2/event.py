# Note: this file can be replaced with an event library
subscribers = dict() # 1

# 2 Import this method to listeners
def subscribe(event_type: str, fn):  
    if not event_type in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)

# 3 Import this method to the subjects
def post_event(event_type: str, data):
    if not event_type in subscribers:
        return
    for fn in subscribers[event_type]:
        fn(data)


