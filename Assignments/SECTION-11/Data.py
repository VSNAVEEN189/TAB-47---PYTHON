'''Data Pipeline

Chaining comprehension steps into a pipeline
Given raw CSV-like strings (rows such as "name,age,score"), build a pipeline where each stage is a one-liner comprehension:
1. parse each row into a dict
2. filter out invalid or low-scoring rows
3. sort by a field
4. format each record into a display string
5. aggregate a summary statistic'''



rows = [
    "Rahul,21,85",
    "Priya,22,92",
    "Amit,20,45",
    "Sneha,23,78",
    "Arjun,19,95",
    "Wrong,data"]

parsed = [
    {
        "name": row.split(",")[0],
        "age": int(row.split(",")[1]),
        "score": int(row.split(",")[2])
    }
    for row in rows
    if len(row.split(",")) == 3]

filtered = [
    student
    for student in parsed
    if student["score"] >= 50]

sorted_students = sorted(
    filtered,
    key=lambda student: student["score"],
    reverse=True)


display = [
    f"{student['name']} - Age: {student['age']} - Score: {student['score']}"
    for student in sorted_students]

average_score = sum(
    student["score"] for student in filtered
) / len(filtered)

print("Parsed:", parsed)
print("Filtered:", filtered)
print("Sorted:", sorted_students)

print("Display:")
for record in display:
    print(record)

print("Average Score:", average_score)