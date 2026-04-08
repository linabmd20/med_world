from collections import defaultdict

from app.db.connection import get_db_connection


def fetch_users_with_accounts():
    conn = None
    cur = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            """
            SELECT
                u.user_id,
                u.full_name,
                u.email,
                a.account_id,
                a.account_type,
                a.balance
            FROM users u
            LEFT JOIN accounts a ON a.user_id = u.user_id
            ORDER BY u.user_id, a.account_id
            """
        )
        rows = cur.fetchall()
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

    users_map = defaultdict(
        lambda: {
            "user_id": None,
            "full_name": None,
            "email": None,
            "accounts": [],
        }
    )

    for user_id, full_name, email, account_id, account_type, balance in rows:
        if users_map[user_id]["user_id"] is None:
            users_map[user_id]["user_id"] = user_id
            users_map[user_id]["full_name"] = full_name
            users_map[user_id]["email"] = email

        if account_id is not None:
            users_map[user_id]["accounts"].append(
                {
                    "account_id": account_id,
                    "account_type": account_type,
                    "balance": float(balance),
                }
            )

    return {"users": list(users_map.values())}
