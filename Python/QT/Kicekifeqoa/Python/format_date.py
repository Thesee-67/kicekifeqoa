from datetime import datetime

def validate_date_format(date_str):
    try:
        return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d 00:00:00")
    except ValueError:
        raise ValueError(f"Format de date invalide : {date_str}. Utilisez le format jj/mm/aaaa.")

def check_dates_consistency(end_date):
    end = datetime.strptime(end_date, "%Y-%m-%d 00:00:00")

def read_date_format(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y")
    except ValueError:
        print(f"Erreur de format de date pour {date_str}")
        return date_str
