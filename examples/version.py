#! [version_short]
version_short('2.6.3')  # returns '2.6'
#! [version_short]

#! [parse_mypy_version normal]
parse_mypy_version('0.930')  # returns (0, 930)
#! [parse_mypy_version normal]

#! [parse_mypy_version dev]
parse_mypy_version(
    '0.940+dev.04cac4b5d911c4f9529e6ce86a27b44f28846f5d.dirty'
)  # returns (0, 940)
#! [parse_mypy_version dev]
