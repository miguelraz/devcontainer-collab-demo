# Zed Demo - Devcontainers!

1. Ask the AI to setup your Dockerfile/`devcontainer.json` dependencies. Make sure to have a docker daemon running.

2. In the Command Palette,  (`Cmd + p > project: open in dev container`) or click the toast on the bottom right. This should install the proper dependencies needed for your setup. In this case, that's `numpy`, `matplotlib`, and `ty` via `uv`.

Write `np.arr` to make sure that the LSPs are working. You should see autocompletion and type hints.

3. Run

```bash
python3 pirates_vs_co2.py
```

and click on the PNG image.

4. Open `data.csv` and then `tabular data: open preview`.