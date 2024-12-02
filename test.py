Traceback (most recent call last):
  File "/home/firstviya/Production/DataLibrary/QuoteMarginYield/QuoteMarginYield.py", line 98, in <module>
    raise e
  File "/home/firstviya/Production/DataLibrary/QuoteMarginYield/QuoteMarginYield.py", line 58, in <module>
    df901 = custhub(df901.copy())
  File "/home/firstviya/Production/venv/lib64/python3.8/site-packages/fifcetllib/fifcfincalclib.py", line 315, in custhub
    df_20.loc[(df_20['ReferralFeeCode_Account'] == 'HUBHKMB')  & (df_20['NF'] < 1000), 'ReferralFee_Account'] = (0 / 100 * df_20['NF'])
  File "/home/firstviya/Production/venv/lib64/python3.8/site-packages/pandas/core/indexing.py", line 716, in __setitem__
    iloc._setitem_with_indexer(indexer, value, self.name)
  File "/home/firstviya/Production/venv/lib64/python3.8/site-packages/pandas/core/indexing.py", line 1688, in _setitem_with_indexer
    self._setitem_with_indexer_split_path(indexer, value, name)
  File "/home/firstviya/Production/venv/lib64/python3.8/site-packages/pandas/core/indexing.py", line 1709, in _setitem_with_indexer_split_path
    value = self._align_series(indexer, Series(value))
  File "/home/firstviya/Production/venv/lib64/python3.8/site-packages/pandas/core/indexing.py", line 2119, in _align_series
    return ser.reindex(new_ix)._values
  File "/home/firstviya/Production/venv/lib64/python3.8/site-packages/pandas/core/series.py", line 4672, in reindex
    return super().reindex(**kwargs)
  File "/home/firstviya/Production/venv/lib64/python3.8/site-packages/pandas/core/generic.py", line 4966, in reindex
    return self._reindex_axes(
  File "/home/firstviya/Production/venv/lib64/python3.8/site-packages/pandas/core/generic.py", line 4986, in _reindex_axes
    obj = obj._reindex_with_indexers(
  File "/home/firstviya/Production/venv/lib64/python3.8/site-packages/pandas/core/generic.py", line 5032, in _reindex_with_indexers
    new_data = new_data.reindex_indexer(
  File "/home/firstviya/Production/venv/lib64/python3.8/site-packages/pandas/core/internals/managers.py", line 679, in reindex_indexer
    self.axes[axis]._validate_can_reindex(indexer)
  File "/home/firstviya/Production/venv/lib64/python3.8/site-packages/pandas/core/indexes/base.py", line 4107, in _validate_can_reindex
    raise ValueError("cannot reindex on an axis with duplicate labels")
ValueError: cannot reindex on an axis with duplicate labels
