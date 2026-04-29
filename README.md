# Text Speaker IO

Text Speaker IO is an open-source web application that enables users to transform and process text, audio, and video content through a unified interface. It supports converting text to speech, speech to text, and other text-based transformations while maintaining a structured history of outputs for each task.

The platform is designed as a modular processing system where a single input can produce multiple outputs, allowing users to experiment with different configurations and results from the same source data.

---

## What It Does

Text Speaker IO allows users to:

- Convert written text into audio (Text-to-Speech)
- Transcribe audio or video into text (Speech-to-Text)
- Process content from multiple input types including raw text, uploaded files, and external video URLs
- Generate multiple outputs from a single input using different configurations
- Access and manage a history of generated outputs for each task (for authenticated users)

---

## Key Features

### Multi-Input Support
- Raw text input
- File uploads (audio, video, text)
- External video URLs (YouTube, Facebook, Reddit, etc.)

---

### Multi-Output System
- Generate multiple results from a single task
- Compare different outputs (e.g., different voices, speeds, or formats)
- Maintain output history per task

---

### Core Processing Capabilities
- Text-to-Speech (TTS)
- Speech-to-Text (STT)
- Text-based transformations (e.g., grammatical corrections, summarization)

---

### File & Media Handling
- Upload and process media files
- Store and manage generated outputs
- Track file metadata such as size and duration

---

### User & Account System
- Optional authentication
- Persistent history for logged-in users
- Anonymous usage without history storage

---

### Plan & Usage Management
- Support for multiple subscription plans
- Configurable limits such as:
  - Maximum text length
  - File size limits
  - Audio duration limits
  - Number of outputs per task

---

### Modular Architecture
- Clean separation between input, processing, and output
- Extensible design for adding new processing types
- Scalable structure aligned with real-world backend systems

---

## Open Source

Text Speaker IO is fully open source.

It is built to explore system design, backend architecture, media processing workflows using Django, and develop experience building AI-powered platforms.

Contributions, ideas, and improvements are welcome ;) .