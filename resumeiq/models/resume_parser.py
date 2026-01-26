def parse_resume(file):
    try:
        content = file.read().decode("utf-8", errors="ignore")
        return content
    except:
        return ""
