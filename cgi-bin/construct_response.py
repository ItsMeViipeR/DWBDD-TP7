def construct_response(code: int, message: str) -> bytes:
    response = f"HTTP/1.1 {code} OK\r\n"
    response += "Content-Type: text/html; charset=utf-8\r\n"
    response += f"Content-Length: {len(message.encode('utf-8'))}\r\n"
    response += "\r\n"
    response += message

    return response.encode("utf-8")
