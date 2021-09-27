import pytchat

vid_id = "VIDEO_ID"
chat = pytchat.create(video_id=vid_id)
while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"{c.message}")