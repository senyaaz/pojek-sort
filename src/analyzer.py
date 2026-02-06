def split_array(arr):
    mid = len(arr) // 2
    return arr[:mid], arr[mid:]

def analyze_half(half, name="Половина"):
    if not half:
        return {"name": name, "size": 0, "sum": 0, "avg": 0}
    
    return {
        "name": name,
        "size": len(half),
        "sum": sum(half),
        "avg": sum(half) / len(half),
        "min": min(half),
        "max": max(half)
    }