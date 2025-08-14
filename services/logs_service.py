from infrastructure.model.log import session, LogModel
from fastapi import HTTPException, status

def create_log(document: dict, log_type: str):
    with session:
        new_log = LogModel(
            document=document,
            log_type=log_type
        )
        session.add(new_log)
        session.commit()

def get_logs():
    return session.query(LogModel).all()

def delete_logs():
    logs = session.query(LogModel).all()
    if logs:
        for log in logs:
            session.delete(log)
        session.commit()
        return {
            "status": "success",
            "message": "Logs were successfully deleted"
        }
    else:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail={
                "status": "error",
                "error": "No logs found"
            }
        )