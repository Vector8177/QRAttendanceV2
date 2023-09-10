from cx_Freeze import setup,Executable

include_files = ['QRCodeAttendanceV2', 'src']

options = {
    'build.exe': {
        'include_files':include_files
    }
}

setup(
    name="QR Attendance",
    version=0.1,
    description="A QR-based attendance system utilizing JSON data storage (local)",
    executables=[Executable("src/main.py", base="Win32GUI")],
    options=options
)