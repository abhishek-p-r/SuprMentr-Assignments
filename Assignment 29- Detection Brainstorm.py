"""
Assignment 29: Detection Brainstorm
Date: 11/04/2026
"""

# -------------------------------
# 5 USES OF FACE / OBJECT DETECTION
# -------------------------------
USES = [
    ("Security & Surveillance", "Automated Attendance System",
     "MTCNN + FaceNet match live faces vs enrolled DB",
     "OpenCV Haar Cascade, FaceNet, MTCNN"),
    
    ("Healthcare / Road Safety", "Driver Drowsiness Detection",
     "EAR < 0.25 for 3+ frames triggers alarm",
     "dlib 68-point landmarks, Eye Aspect Ratio"),
    
    ("Retail & Commerce", "Smart Shelf Inventory Monitor",
     "YOLO detects product count; alert when low",
     "YOLOv8, TF Object Detection API, RTSP"),
    
    ("Agriculture", "Crop Disease & Pest Detection",
     "Drone CNN classifies diseased leaf regions",
     "ResNet, Mask R-CNN, UAV imagery"),
    
    ("Public Safety", "Crowd Density Monitor",
     "Bounding box centroids flag pairs < 1.5 m",
     "YOLOv5, DeepSORT, perspective transform"),
]

print("5 USES OF FACE / OBJECT DETECTION".center(80))
for i, (domain, use, how, tech) in enumerate(USES, 1):
    print(f"\n{i}. {use}")
    print(f"   Domain : {domain}")
    print(f"   How    : {how}")
    print(f"   Tech   : {tech}")

# -------------------------------
# DESIGNED SOLUTION
# -------------------------------
print("\nDESIGNED SOLUTION: SmartAttend – Classroom Attendance".center(80))

PIPELINE = [
    ("Step 1", "Enrolment",   "Capture 5 face photos per student"),
    ("Step 2", "Encoding",    "FaceNet → 128-dim embedding vector"),
    ("Step 3", "Detection",   "MTCNN detects & aligns faces in class photo"),
    ("Step 4", "Recognition", "Cosine similarity vs stored embeddings"),
    ("Step 5", "Threshold",   "Score > 0.85 → mark present in DB"),
    ("Step 6", "Report",      "Auto-export CSV/PDF attendance sheet"),
]

print("\nPipeline Steps:")
for step, name, detail in PIPELINE:
    print(f"  {step} – {name:<14}: {detail}")

# -------------------------------
# PSEUDOCODE
# -------------------------------
print("\nPSEUDOCODE:")

pseudocode = [
    "for student in enrolled_students:",
    "    embeddings[student.id] = facenet_encode(5_photos).mean()",
    "",
    "class_photo  = camera.capture()",
    "face_crops   = mtcnn.detect(class_photo)",
    "for face in face_crops:",
    "    scores  = cosine_sim(facenet_encode(face), embeddings)",
    "    best    = max(scores, key=scores.get)",
    "    if scores[best] > 0.85: db.mark_present(best)",
    "    else: flag_unknown(face)",
    "",
    "db.export_report(class_id, date)",
]

for line in pseudocode:
    print(f"  {line}")

# -------------------------------
# STACK & TARGETS
# -------------------------------
STACK = [
    ("Detection", "MTCNN — 3-stage CNN"),
    ("Recognition", "FaceNet 128-dim embeddings"),
    ("Similarity", "Cosine similarity"),
    ("Storage", "SQLite / PostgreSQL"),
    ("Interface", "Streamlit dashboard"),
    ("Hardware", "Pi4 + HD camera / webcam")
]

print("\nSTACK:")
for k, v in STACK:
    print(f"  {k:<14}: {v}")

print("\nTARGETS: Accuracy >97%  |  Speed <500ms  |  Saves 8 min/class")