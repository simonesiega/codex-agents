def build_sales_report(rows):
    total = 0
    lines = []

    for row in rows:
        total += row["amount"]
        lines.append(f"{row['date']},{row['customer']},{row['amount']}")

    return "\n".join(lines) + f"\nTOTAL,,{total}"
