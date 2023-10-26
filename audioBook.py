import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

name = str(input("Enter Your Name : "))
age = str(input("Enter Your Age : "))
profession = str(input("Enter Your Profession : "))

speaker.Speak(f"Hello, I am {name} and I am {age} years old. I am currently a {profession}")
print(f"Hello, I am {name} and I am {age} years old. I am currently a {profession}")