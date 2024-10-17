from datetime import datetime

def validate_date_format(date_str):
    try:
        return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d 00:00:00")
    except ValueError:
        raise ValueError(f"Format de date invalide : {date_str}. Utilisez le format jj/mm/aaaa.")

def check_dates_consistency(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d 00:00:00")
    end = datetime.strptime(end_date, "%Y-%m-%d 00:00:00")
    if start > end:
        raise ValueError("La date de début ne peut pas être postérieure à la date de fin.")
