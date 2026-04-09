python

timesteps = 50  # ps per frame
n_frames = cmd.count_states()

cmd.remove("forLabel")
cmd.delete("forLabel")

for frame in range(1, n_frames + 1):
    time_ns = ((frame - 1) * timesteps )/ 1000       # to show time in nanoseconds (ns)

    # Show "0 ns" for first frame, "X.XXX ns" for the rest
    label_text = "0 ns" if time_ns == 0 else f"{time_ns:.3f} ns"

    cmd.pseudoatom(
        "forLabel",
        pos=[70, 100, 100],                      # position of the label
        state=frame,
        label=label_text
    )

cmd.label("forLabel", "label")

cmd.set("label_color", "black", "forLabel")
cmd.set("label_size",  20,      "forLabel")
cmd.set("label_font_id", 7)

cmd.hide("everything", "forLabel")
cmd.show("labels",     "forLabel")

# cmd.mplay()

python end