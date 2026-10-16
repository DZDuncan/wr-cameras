# wr-cameras

Quick proof of concept for streaming using GStreamer & RTSP.

If you are on VSCode, you may need to add the following to your `settings.json`:
```json
"terminal.integrated.env.linux": {
	"GTK_PATH": null,
	"GIO_MODULE_DIR": null
}
```

OpenCV is currently included as a package but this is temporary (for prototyping). It will be removed later.