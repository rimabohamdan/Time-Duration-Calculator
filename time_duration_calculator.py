seconds = int(input("Enter the duration in seconds :\n"))
hours = seconds // 3600
# الدقائق اي باقي القسمة
minutes = (seconds % 3600) // 60
# قسمت الثواني على 3600 طلعت الساعات
remaining_seconds = seconds % 60
# تجاهلت الرقم الصحيح شفت قدي ضل
# العدد الي لا يمكن ادماجه في الدقائق هو الثواني اي اقل من 60
print("The duration is:")
print(f"{hours} hours, {minutes} minutes, and {remaining_seconds} seconds.")
