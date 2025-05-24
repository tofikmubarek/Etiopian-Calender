from ethiopian_date import EthiopianDate, EthiopianDateConverter
from datetime import date

def main():
    print("Ethiopian <-> Gregorian Calendar Converter")
    print("1. Ethiopian to Gregorian")
    print("2. Gregorian to Ethiopian")
    choice = input("Choose conversion (1 or 2): ").strip()

    if choice == "1":
        try:
            y = int(input("Enter Ethiopian year: "))
            m = int(input("Enter Ethiopian month: "))
            d = int(input("Enter Ethiopian day: "))
            et_date = EthiopianDate(y, m, d)
            print(f"Gregorian date: {et_date.local_date}")
        except Exception as e:
            print(f"Error: {e}")
    elif choice == "2":
        try:
            y = int(input("Enter Gregorian year: "))
            m = int(input("Enter Gregorian month: "))
            d = int(input("Enter Gregorian day: "))
            gr_date = date(y, m, d)
            et_date = EthiopianDate(local_date=gr_date)
            print(f"Ethiopian date: {et_date.year}-{et_date.month}-{et_date.day}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
