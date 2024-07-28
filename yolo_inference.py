from ultralytics import YOLO

# Test the model on the video and print out results
# Print out results for first frame
# Every object found has classifying id, confidentiality of result and
# bounding box



model = YOLO('models/local_gpu/best.pt')

results = model.predict('input_videos/08fd33_4.mp4', device='0', save=True)
print(results[0])
print("=========================")

for box in results[0].boxes:
    print(box)