import os

from paperwhisperer.tts.utils import save_file


class TTSProcessor:
    """TTSProcessor is responsible to apply text-to-speech to the
    description of a list of articles and save the result to disk."""

    def __init__(self, speech_synthesizer, save_dir):
        self.speech_synthesizer = speech_synthesizer
        self.save_dir = save_dir

    def synthesise_and_save(self, articles):
        for i, article in enumerate(articles):
            speech_content = self._synthesise_article(article.description)
            print(f"Article with title '{article.title}' converted to speech")
            save_path = os.path.join(self.save_dir, f"{i+1}.mp3")
            save_file(save_path, speech_content)
            print(f"Speech conversion saved at '{save_path}'")

    def _synthesise_article(self, article_description):
        return self.speech_synthesizer.synthesise(article_description)