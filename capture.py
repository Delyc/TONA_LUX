import subprocess

def capture_image(filename="skin_image.jpg"):
    subprocess.run(
        ["rpicam-still", "-n", "-o", filename],
        check=True
    )
    print(f"Image saved: {filename}")

if __name__ == "__main__":
    capture_image()