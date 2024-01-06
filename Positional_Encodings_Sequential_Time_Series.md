
# Using Positional Encodings for Sequential Time Series Data

## Purpose of Positional Encodings
- Transformers lack an inherent mechanism to recognize the order of inputs in a sequence. Positional encodings provide information about the sequence order to the Transformer.

## Generating Positional Encodings
- Positional encodings are generated using sinusoidal functions of different frequencies for each position `pos` in the sequence and dimension `i` in the embedding.
- The formulas for positional encoding `pos_enc` are:
  - `pos_enc(pos, 2i) = sin(pos / 10000^(2i/d_model))`
  - `pos_enc(pos, 2i+1) = cos(pos / 10000^(2i/d_model))`
- `d_model` is the dimension of the embedding, and `pos` is the position in the sequence.

## Applying Positional Encodings
- The positional encoding vector is added to the input embedding vector for each time step in the sequence.
- The `pos` value corresponds to the temporal order in the sequence.
- For different time steps in a sequence, `pos` is calculated accordingly (e.g., 0 for the first day, 1 for the second day, etc.).

## Handling Different Sequence Lengths
- Generate positional encodings up to the maximum sequence length to accommodate sequences of different lengths.
- Apply masking in the Transformer to ignore padded positions in sequences.

## Training and Prediction
- Ensure that each input sequence to the Transformer has the correct positional encodings added during both training and prediction.
- This approach allows the model to understand the temporal relationship between different time steps in the sequence.

Positional encodings are crucial for the Transformer to understand the order of events in time series data, making more informed predictions.
