import hashlib
import io
import os
import importlib
import sys
import builtins
import pytest
from pathlib import Path
import main

#Written by ChatGPT, functions as necessary to provide adequate testing for my code.

def write_file(path: Path, lines):
    path.write_text("\n".join(lines) + ("\n" if lines and not str(lines[-1]).endswith("\n") else ""))


def test_md5_crack(tmp_path, capsys):
    # prepare wordlist and hash file
    wordlist = tmp_path / "words.txt"
    target = "secret123"
    words = ["hello", "world", target, "password"]
    write_file(wordlist, words)

    # compute md5 of target and write to hash file
    digest = hashlib.md5(target.encode()).hexdigest()
    hashfile = tmp_path / "hashes.txt"
    write_file(hashfile, [digest])

    # call function and capture output
    main.md5(str(hashfile), str(wordlist))
    captured = capsys.readouterr()
    assert "[+] Cracked" in captured.out
    assert "secret123" in captured.out


def test_sha256_crack(tmp_path, capsys):
    wordlist = tmp_path / "words2.txt"
    target = "hunter2"
    words = ["alpha", target, "beta"]
    write_file(wordlist, words)

    digest = hashlib.sha256(target.encode()).hexdigest()
    hashfile = tmp_path / "hashes2.txt"
    write_file(hashfile, [digest])

    main.sha256(str(hashfile), str(wordlist))
    captured = capsys.readouterr()
    assert "[+] Cracked" in captured.out
    assert "hunter2" in captured.out


def test_sha1_failure(tmp_path, capsys):
    # create a hash that does NOT match any word in the wordlist
    wordlist = tmp_path / "wl.txt"
    words = ["one", "two", "three"]
    write_file(wordlist, words)

    # random sha1 that won't match (e.g., sha1 of "nobody")
    not_password = "nobody"
    digest = hashlib.sha1(not_password.encode()).hexdigest()
    hashfile = tmp_path / "hashes3.txt"
    write_file(hashfile, [digest])

    # but wordlist doesn't contain "nobody", so it should fail
    main.sha1(str(hashfile), str(wordlist))
    captured = capsys.readouterr()
    assert "Failed" in captured.out or "Failed -- >" in captured.out


def test_main_flow_md5(tmp_path, monkeypatch, capsys):
    # full main() flow using md5
    wordlist = tmp_path / "wl_main.txt"
    target = "letmein"
    write_file(wordlist, ["foo", target, "bar"])

    digest = hashlib.md5(target.encode()).hexdigest()
    hashfile = tmp_path / "hf_main.txt"
    write_file(hashfile, [digest])

    # prepare input sequence: hash_file_path, wordlist_path, algorithm
    inputs = iter([str(hashfile), str(wordlist), "md5"])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(inputs))

    # run main()
    main.main()
    captured = capsys.readouterr()
    assert "[+] Cracked" in captured.out
    assert "letmein" in captured.out


def test_main_invalid_then_valid(tmp_path, monkeypatch, capsys):
    # test that an invalid algorithm causes the program to ask again (main calls main() recursively)
    wordlist = tmp_path / "wl_chain.txt"
    target = "open_sesame"
    write_file(wordlist, ["x", target])

    digest = hashlib.sha256(target.encode()).hexdigest()
    hashfile = tmp_path / "hf_chain.txt"
    write_file(hashfile, [digest])

    # Provide two rounds of inputs:
    # 1) invalid algorithm -> program prints error and calls main() again
    # 2) valid algorithm sha256
    inputs = iter([
        str(hashfile), str(wordlist), "not_an_algo",   # first main() call - invalid
        str(hashfile), str(wordlist), "sha256"        # second main() call - valid
    ])
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(inputs))

    main.main()
    captured = capsys.readouterr()
    # Should contain failure message for invalid algorithm
    assert "You did not input a valid hashing algorithm" in captured.out
    # And then should have cracked the sha256 in the second attempt
    assert "[+] Cracked" in captured.out
    assert "open_sesame" in captured.out
