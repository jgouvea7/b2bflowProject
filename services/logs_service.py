from infrastructure.model.log import session, LogModel

def create_log(document: dict, log_type: str):
    with session:
        new_log = LogModel(
            document=document,
            log_type=log_type
        )
        session.add(new_log)
        session.commit()

def get_logs():
    logs =  session.query(LogModel).all()
    if logs:
        return logs
    else:
        return {
            "status": "error",
            "error": "No logs found"
        }

def delete_logs():
    logs = session.query(LogModel).all()
    for log in logs:
        session.delete(log)
    session.commit()
    return {
        "status": "success",
        "message": "Logs were successfully deleted"
    }