import h5py

# Open the compressed HDF5 file in read mode
with h5py.File('compressed_file.h5', 'r') as compressed_file:
    # Create a new HDF5 file for extracted data in write mode
    with h5py.File('mnist.h5', 'w') as extracted_file:
        # Iterate over all items in the compressed file
        for item_name, item in compressed_file.items():
            # Check if the item is a dataset
            if isinstance(item, h5py.Dataset):
                # Create a new dataset in the extracted file
                extracted_dataset = extracted_file.create_dataset(
                    item_name,
                    shape=item.shape,
                    dtype=item.dtype
                )

                # Copy the data from the compressed dataset to the extracted dataset
                extracted_dataset[...] = item[...]

print("Extraction complete.")
