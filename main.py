import pytchat

vid_id = "uxPQPp_nAs0"
chat = pytchat.create(video_id=vid_id)
while chat.is_alive():
    for c in chat.get().sync_items():
        if c.message.startswith("/"):
            print(f"{c.message}")