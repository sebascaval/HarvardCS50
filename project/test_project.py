import project
import pytest

song= project.get_lyrics("Ed Sheeran","Perfect")

def test_get_lyrics():
    with pytest.raises(ValueError):
        project.get_lyrics("","")

    assert "******* This Lyrics is NOT for Commercial use *******" not in song
    assert "..." not in song

if __name__ == "__main__":
    pytest.main()