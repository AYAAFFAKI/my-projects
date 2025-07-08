import cv2
def draw_gaze_bar(frame, counts, position= (20,80)):
    labels = ['Left','Center','Right']
    total = sum(counts.values()) if sum(counts.values()) >0 else 1

    x,y = position
    bar_width = 300
    bar_height = 20
    spacing = 10

    for i, label in enumerate(labels):
        proportion= counts[label]/total
        length = int(proportion * bar_width)
        color = (255,0,0) if label =='Left' else (0,255,0) if label =='Center' else (0,0,255)

        y_offset = y+i * (bar_height*spacing)
        cv2.rectangle(frame,(x,y_offset),(x+length,y_offset+bar_height),color,-1)

        cv2.putText(frame, f'{label}:{counts[label]}',
                    (x+ length+10, y_offset+bar_height-5),
                    cv2.FONT_HERSHEY_SIMPLEX,0.5, color,1)
