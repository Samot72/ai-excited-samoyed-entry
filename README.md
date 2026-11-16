# ai-excited-01 — He smashed his own frame to bring you a birthday cake, Judge

A giant fluffy Samoyed bursts through his own shattered picture frame, paws outstretched toward the viewer, proudly delivering a birthday cake with lit candles. The entry program (main.ts) copies entry.png to the output directory, byte for byte. entry.png is built deterministically by make_image.py, which converts the source artwork to RGB and resizes it with LANCZOS resampling to the largest width whose PNG fits the competition's size cap.
