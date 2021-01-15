"""Autogenerated DPF operator classes.

Created on 01/15/2021, 00:24:02
"""
from collections import OrderedDict
from collections import namedtuple
from ansys.dpf import core as dpf

InputSpec = namedtuple('InputSpec', ['document', 'ellipsis', 'name', 'optional',
                                     'type_names'])

OutputSpec = namedtuple('OutputSpec', ['name', 'type_names', 'document'])


class ResultInfoProvider(dpf.Operator):
    """DPF "ResultInfoProvider" Operator

    Read the result info with information sucha as available results
    or unit system from the results files contained in the streams or
    data sources.

    Available inputs:
     -   ``data_sources`` : DataSources
         If the stream is null then we need to get the file path from the data
         sources

     -   ``streams_container`` : StreamsContainer, optional
         Streams (result file container) (optional)


    Available outputs:
     -   result_info


    Parameters
    ----------
    data_sources : DataSources
        If the stream is null then we need to get the file path from
        the data sources

    streams_container : streams_container, optional
        Streams (result file container) (optional)

    Examples
    --------
    >>> op = dpf.operators.ResultInfoProvider()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> op.inputs.streams_container.connect(my_streams_container)  # optional
    >>> my_result_info = op.outputs.result_info()
    """

    class _Inputs(dpf.inputs.Inputs):
        _spec = OrderedDict([(3, InputSpec(document='streams (result file container) (optional)', ellipsis=False, name='streams_container', optional=True, type_names=['streams_container'])), (4, InputSpec(document='if the stream is null then we need to get the file path from the data sources', ellipsis=False, name='data_sources', optional=False, type_names=['data_sources']))])
        def __init__(self, oper):
            self._streams_container = None
            self._data_sources = None
            super().__init__(self._spec, oper)

        @property
        def streams_container(self):
            """streams (result file container) (optional)"""
            return self._streams_container

        @streams_container.setter
        def streams_container(self, streams_container):
            self._streams_container.connect(streams_container)

        @property
        def data_sources(self):
            """if the stream is null then we need to get the file path from the data sources"""
            return self._data_sources

        @data_sources.setter
        def data_sources(self, data_sources):
            self._data_sources.connect(data_sources)


    class _Outputs(dpf.outputs.Outputs):
        _spec = OrderedDict([(0, OutputSpec(name='result_info', type_names=['result_info'], document=''))])
        def __init__(self, oper):
            self._result_info = None
            super().__init__(self._spec, oper)

        @property
        def result_info(self):
            """"""
            return self._result_info


    def __init__(self, data_sources, streams_container=None):
        if channel is None:
            channel = dpf.server._global_channel()

        self._channel = channel
        self._stub = self._connect()
        self._message = None
        self._description = None
        self.name = "ResultInfoProvider"

        self._Operator__send_init_request()

        self.inputs = self._Inputs(self)
        self.outputs = self._Outputs(self)

    @property
    def result_info(self):
        """"""
        return self.outputs._result_info



class TimeFreqProvider(dpf.Operator):
    """DPF "TimeFreqSupportProvider" Operator

    Read the time freq support from the results files contained in the
    streams or data sources.

    Available inputs:
     -   ``data_sources`` : DataSources
         If the stream is null then we need to get the file path from the data
         sources

     -   ``streams_container`` : StreamsContainer, optional
         Streams (result file container) (optional)


    Available outputs:
     -   time_freq_support


    Parameters
    ----------
    data_sources : DataSources
        If the stream is null then we need to get the file path from
        the data sources

    streams_container : streams_container, optional
        Streams (result file container) (optional)

    Examples
    --------
    >>> op = dpf.operators.TimeFreqProvider()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> op.inputs.streams_container.connect(my_streams_container)  # optional
    >>> my_time_freq_support = op.outputs.time_freq_support()
    """

    class _Inputs(dpf.inputs.Inputs):
        _spec = OrderedDict([(3, InputSpec(document='streams (result file container) (optional)', ellipsis=False, name='streams_container', optional=True, type_names=['streams_container'])), (4, InputSpec(document='if the stream is null then we need to get the file path from the data sources', ellipsis=False, name='data_sources', optional=False, type_names=['data_sources']))])
        def __init__(self, oper):
            self._streams_container = None
            self._data_sources = None
            super().__init__(self._spec, oper)

        @property
        def streams_container(self):
            """streams (result file container) (optional)"""
            return self._streams_container

        @streams_container.setter
        def streams_container(self, streams_container):
            self._streams_container.connect(streams_container)

        @property
        def data_sources(self):
            """if the stream is null then we need to get the file path from the data sources"""
            return self._data_sources

        @data_sources.setter
        def data_sources(self, data_sources):
            self._data_sources.connect(data_sources)


    class _Outputs(dpf.outputs.Outputs):
        _spec = OrderedDict([(0, OutputSpec(name='time_freq_support', type_names=['time_freq_support'], document=''))])
        def __init__(self, oper):
            self._time_freq_support = None
            super().__init__(self._spec, oper)

        @property
        def time_freq_support(self):
            """"""
            return self._time_freq_support


    def __init__(self, data_sources, streams_container=None):
        if channel is None:
            channel = dpf.server._global_channel()

        self._channel = channel
        self._stub = self._connect()
        self._message = None
        self._description = None
        self.name = "TimeFreqSupportProvider"

        self._Operator__send_init_request()

        self.inputs = self._Inputs(self)
        self.outputs = self._Outputs(self)

    @property
    def time_freq_support(self):
        """"""
        return self.outputs._time_freq_support



class MaterialProvider(dpf.Operator):
    """DPF "MaterialsProvider" Operator

    Read available materials and properties from the results files
    contained in the streams or data sources.

    Available inputs:
     -   ``streams_container`` : StreamsContainer, optional
         Streams (result file container)

     -   ``data_sources`` : DataSources
         If the stream is null then we need to get the file path from the data
         sources


    Available outputs:
     -   materials


    Parameters
    ----------
    data_sources : DataSources
        If the stream is null then we need to get the file path from
        the data sources

    streams_container : streams_container, optional
        Streams (result file container)

    Examples
    --------
    >>> op = dpf.operators.MaterialProvider()
    >>> op.inputs.streams_container.connect(my_streams_container)  # optional
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_materials = op.outputs.materials()
    """

    class _Inputs(dpf.inputs.Inputs):
        _spec = OrderedDict([(3, InputSpec(document='streams (result file container)', ellipsis=False, name='streams_container', optional=True, type_names=['streams_container'])), (4, InputSpec(document='if the stream is null then we need to get the file path from the data sources', ellipsis=False, name='data_sources', optional=False, type_names=['data_sources']))])
        def __init__(self, oper):
            self._streams_container = None
            self._data_sources = None
            super().__init__(self._spec, oper)

        @property
        def streams_container(self):
            """streams (result file container)"""
            return self._streams_container

        @streams_container.setter
        def streams_container(self, streams_container):
            self._streams_container.connect(streams_container)

        @property
        def data_sources(self):
            """if the stream is null then we need to get the file path from the data sources"""
            return self._data_sources

        @data_sources.setter
        def data_sources(self, data_sources):
            self._data_sources.connect(data_sources)


    class _Outputs(dpf.outputs.Outputs):
        _spec = OrderedDict([(0, OutputSpec(name='materials', type_names=['materials'], document=''))])
        def __init__(self, oper):
            self._materials = None
            super().__init__(self._spec, oper)

        @property
        def materials(self):
            """"""
            return self._materials


    def __init__(self, data_sources, streams_container=None):
        if channel is None:
            channel = dpf.server._global_channel()

        self._channel = channel
        self._stub = self._connect()
        self._message = None
        self._description = None
        self.name = "MaterialsProvider"

        self._Operator__send_init_request()

        self.inputs = self._Inputs(self)
        self.outputs = self._Outputs(self)

    @property
    def materials(self):
        """"""
        return self.outputs._materials



class StreamsProvider(dpf.Operator):
    """DPF "stream_provider" Operator

    Creates streams (files with cache) from the data sources.

    Available inputs:
     -   ``data_sources`` : DataSources


    Available outputs:
     -   streams_container


    Parameters
    ----------
    data_sources : DataSources




    Examples
    --------
    >>> op = dpf.operators.StreamsProvider()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_streams_container = op.outputs.streams_container()
    """

    class _Inputs(dpf.inputs.Inputs):
        _spec = OrderedDict([(4, InputSpec(document='', ellipsis=False, name='data_sources', optional=False, type_names=['data_sources']))])
        def __init__(self, oper):
            self._data_sources = None
            super().__init__(self._spec, oper)

        @property
        def data_sources(self):
            return self._data_sources

        @data_sources.setter
        def data_sources(self, data_sources):
            self._data_sources.connect(data_sources)


    class _Outputs(dpf.outputs.Outputs):
        _spec = OrderedDict([(0, OutputSpec(name='streams_container', type_names=['streams_container'], document=''))])
        def __init__(self, oper):
            self._streams_container = None
            super().__init__(self._spec, oper)

        @property
        def streams_container(self):
            """"""
            return self._streams_container


    def __init__(self, data_sources):
        if channel is None:
            channel = dpf.server._global_channel()

        self._channel = channel
        self._stub = self._connect()
        self._message = None
        self._description = None
        self.name = "stream_provider"

        self._Operator__send_init_request()

        self.inputs = self._Inputs(self)
        self.outputs = self._Outputs(self)

    @property
    def streams_container(self):
        """"""
        return self.outputs._streams_container



class MeshSelectionManagerProvider(dpf.Operator):
    """DPF "MeshSelectionManagerProvider" Operator

    Read mesh properties from the results files contained in the
    streams or data sources and make those properties available
    through a mesh selection manager in output.

    Available inputs:
     -   ``data_sources`` : DataSources
         If the stream is null then we need to get the file path from the data
         sources

     -   ``streams_container`` : StreamsContainer, optional
         Streams (result file container) (optional)


    Available outputs:
     -   mesh_selection_manager


    Parameters
    ----------
    data_sources : DataSources
        If the stream is null then we need to get the file path from
        the data sources

    streams_container : streams_container, optional
        Streams (result file container) (optional)

    Examples
    --------
    >>> op = dpf.operators.MeshSelectionManagerProvider()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> op.inputs.streams_container.connect(my_streams_container)  # optional
    >>> my_mesh_selection_manager = op.outputs.mesh_selection_manager()
    """

    class _Inputs(dpf.inputs.Inputs):
        _spec = OrderedDict([(3, InputSpec(document='streams (result file container) (optional)', ellipsis=False, name='streams_container', optional=True, type_names=['streams_container'])), (4, InputSpec(document='if the stream is null then we need to get the file path from the data sources', ellipsis=False, name='data_sources', optional=False, type_names=['data_sources']))])
        def __init__(self, oper):
            self._streams_container = None
            self._data_sources = None
            super().__init__(self._spec, oper)

        @property
        def streams_container(self):
            """streams (result file container) (optional)"""
            return self._streams_container

        @streams_container.setter
        def streams_container(self, streams_container):
            self._streams_container.connect(streams_container)

        @property
        def data_sources(self):
            """if the stream is null then we need to get the file path from the data sources"""
            return self._data_sources

        @data_sources.setter
        def data_sources(self, data_sources):
            self._data_sources.connect(data_sources)


    class _Outputs(dpf.outputs.Outputs):
        _spec = OrderedDict([(0, OutputSpec(name='mesh_selection_manager', type_names=['N14dataProcessing21CMeshSelectionManagerE'], document=''))])
        def __init__(self, oper):
            self._mesh_selection_manager = None
            super().__init__(self._spec, oper)

        @property
        def mesh_selection_manager(self):
            """"""
            return self._mesh_selection_manager


    def __init__(self, data_sources, streams_container=None):
        if channel is None:
            channel = dpf.server._global_channel()

        self._channel = channel
        self._stub = self._connect()
        self._message = None
        self._description = None
        self.name = "MeshSelectionManagerProvider"

        self._Operator__send_init_request()

        self.inputs = self._Inputs(self)
        self.outputs = self._Outputs(self)

    @property
    def mesh_selection_manager(self):
        """"""
        return self.outputs._mesh_selection_manager



class BoundaryConditionProvider(dpf.Operator):
    """DPF "boundary_conditions" Operator

    Read boundary conditions from the results files contained in the
    streams or data sources.

    Available inputs:
     -   ``data_sources`` : DataSources

     -   ``streams_container`` : StreamsContainer, optional


    Available outputs:
     -   results_info


    Parameters
    ----------
    data_sources : DataSources


    streams_container : streams_container, optional


    Examples
    --------
    >>> op = dpf.operators.BoundaryConditionProvider()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> op.inputs.streams_container.connect(my_streams_container)  # optional
    >>> my_results_info = op.outputs.results_info()
    """

    class _Inputs(dpf.inputs.Inputs):
        _spec = OrderedDict([(3, InputSpec(document='', ellipsis=False, name='streams_container', optional=True, type_names=['streams_container'])), (4, InputSpec(document='', ellipsis=False, name='data_sources', optional=False, type_names=['data_sources']))])
        def __init__(self, oper):
            self._streams_container = None
            self._data_sources = None
            super().__init__(self._spec, oper)

        @property
        def streams_container(self):
            return self._streams_container

        @streams_container.setter
        def streams_container(self, streams_container):
            self._streams_container.connect(streams_container)

        @property
        def data_sources(self):
            return self._data_sources

        @data_sources.setter
        def data_sources(self, data_sources):
            self._data_sources.connect(data_sources)


    class _Outputs(dpf.outputs.Outputs):
        _spec = OrderedDict([(0, OutputSpec(name='results_info', type_names=['field', 'fields_container'], document='results info'))])
        def __init__(self, oper):
            self._results_info = None
            super().__init__(self._spec, oper)

        @property
        def results_info(self):
            """results info"""
            return self._results_info


    def __init__(self, data_sources, streams_container=None):
        if channel is None:
            channel = dpf.server._global_channel()

        self._channel = channel
        self._stub = self._connect()
        self._message = None
        self._description = None
        self.name = "boundary_conditions"

        self._Operator__send_init_request()

        self.inputs = self._Inputs(self)
        self.outputs = self._Outputs(self)

    @property
    def results_info(self):
        """results info"""
        return self.outputs._results_info



class IsCyclic(dpf.Operator):
    """DPF "is_cyclic" Operator

    Read if the model is cyclic form the result file.

    Available inputs:
     -   ``data_sources`` : DataSources
         If the stream is null then we need to get the file path from the data
         sources

     -   ``streams_container`` : StreamsContainer, optional
         Streams (result file container) (optional)


    Available outputs:
     -   file_path


    Parameters
    ----------
    data_sources : DataSources
        If the stream is null then we need to get the file path from
        the data sources

    streams_container : streams_container, optional
        Streams (result file container) (optional)

    Examples
    --------
    >>> op = dpf.operators.IsCyclic()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> op.inputs.streams_container.connect(my_streams_container)  # optional
    >>> my_file_path = op.outputs.file_path()
    """

    class _Inputs(dpf.inputs.Inputs):
        _spec = OrderedDict([(3, InputSpec(document='streams (result file container) (optional)', ellipsis=False, name='streams_container', optional=True, type_names=['streams_container'])), (4, InputSpec(document='if the stream is null then we need to get the file path from the data sources', ellipsis=False, name='data_sources', optional=False, type_names=['data_sources']))])
        def __init__(self, oper):
            self._streams_container = None
            self._data_sources = None
            super().__init__(self._spec, oper)

        @property
        def streams_container(self):
            """streams (result file container) (optional)"""
            return self._streams_container

        @streams_container.setter
        def streams_container(self, streams_container):
            self._streams_container.connect(streams_container)

        @property
        def data_sources(self):
            """if the stream is null then we need to get the file path from the data sources"""
            return self._data_sources

        @data_sources.setter
        def data_sources(self, data_sources):
            self._data_sources.connect(data_sources)


    class _Outputs(dpf.outputs.Outputs):
        _spec = OrderedDict([(0, OutputSpec(name='file_path', type_names=['string'], document="returns 'single_stage' or 'multi_stage' or an empty string for non cyclic model"))])
        def __init__(self, oper):
            self._file_path = None
            super().__init__(self._spec, oper)

        @property
        def file_path(self):
            """returns 'single_stage' or 'multi_stage' or an empty string for non cyclic model"""
            return self._file_path


    def __init__(self, data_sources, streams_container=None):
        if channel is None:
            channel = dpf.server._global_channel()

        self._channel = channel
        self._stub = self._connect()
        self._message = None
        self._description = None
        self.name = "is_cyclic"

        self._Operator__send_init_request()

        self.inputs = self._Inputs(self)
        self.outputs = self._Outputs(self)

    @property
    def file_path(self):
        """returns 'single_stage' or 'multi_stage' or an empty string for non cyclic model"""
        return self.outputs._file_path



class CyclicSupportProvider(dpf.Operator):
    """DPF "mapdl::rst::support_provider_cyclic" Operator

    Read the cyclic support (DPF entity containing necessary
    informations for expansions) and expands the mesh.

    Available inputs:
     -   ``sector_meshed_region`` : MeshedRegion, optional
         Mesh of the first sector.

     -   ``streams_container`` : StreamsContainer, optional
         Streams containing the result file.

     -   ``sectors_to_expand`` : Scoping, ScopingsContainer, list, optional
         Sectors to expand (start at 0), for multistage: use scopings container
         with 'stage' label.

     -   ``expanded_meshed_region`` : MeshedRegion, optional
         If this pin is set, expanding the mesh is not necessary.

     -   ``data_sources`` : DataSources
         Data sources containing the result file.


    Available outputs:
     -   sector_meshed_region
     -   cyclic_support


    Parameters
    ----------
    data_sources : DataSources
        Data sources containing the result file.

    streams_container : streams_container, optional
        Streams containing the result file.

    sector_meshed_region : MeshedRegion, optional
        Mesh of the first sector.

    expanded_meshed_region : MeshedRegion, optional
        If this pin is set, expanding the mesh is not necessary.

    sectors_to_expand : Scoping or scopings_container or list, optional
        Sectors to expand (start at 0), for multistage: use scopings
        container with 'stage' label.

    Examples
    --------
    >>> op = dpf.operators.CyclicSupportProvider()
    >>> op.inputs.sector_meshed_region.connect(my_sector_meshed_region)  # optional
    >>> op.inputs.streams_container.connect(my_streams_container)  # optional
    >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)  # optional
    >>> op.inputs.expanded_meshed_region.connect(my_expanded_meshed_region)  # optional
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_sector_meshed_region = op.outputs.sector_meshed_region()
    >>> my_cyclic_support = op.outputs.cyclic_support()
    """

    class _Inputs(dpf.inputs.Inputs):
        _spec = OrderedDict([(3, InputSpec(document='Streams containing the result file.', ellipsis=False, name='streams_container', optional=True, type_names=['streams_container'])), (4, InputSpec(document='data sources containing the result file.', ellipsis=False, name='data_sources', optional=False, type_names=['data_sources'])), (7, InputSpec(document='mesh of the first sector.', ellipsis=False, name='sector_meshed_region', optional=True, type_names=['abstract_meshed_region'])), (15, InputSpec(document='if this pin is set, expanding the mesh is not necessary.', ellipsis=False, name='expanded_meshed_region', optional=True, type_names=['abstract_meshed_region'])), (18, InputSpec(document="sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.", ellipsis=False, name='sectors_to_expand', optional=True, type_names=['scoping', 'scopings_container', 'vector<int32>']))])
        def __init__(self, oper):
            self._streams_container = None
            self._data_sources = None
            self._sector_meshed_region = None
            self._expanded_meshed_region = None
            self._sectors_to_expand = None
            super().__init__(self._spec, oper)

        @property
        def streams_container(self):
            """Streams containing the result file."""
            return self._streams_container

        @streams_container.setter
        def streams_container(self, streams_container):
            self._streams_container.connect(streams_container)

        @property
        def data_sources(self):
            """data sources containing the result file."""
            return self._data_sources

        @data_sources.setter
        def data_sources(self, data_sources):
            self._data_sources.connect(data_sources)

        @property
        def sector_meshed_region(self):
            """mesh of the first sector."""
            return self._sector_meshed_region

        @sector_meshed_region.setter
        def sector_meshed_region(self, sector_meshed_region):
            self._sector_meshed_region.connect(sector_meshed_region)

        @property
        def expanded_meshed_region(self):
            """if this pin is set, expanding the mesh is not necessary."""
            return self._expanded_meshed_region

        @expanded_meshed_region.setter
        def expanded_meshed_region(self, expanded_meshed_region):
            self._expanded_meshed_region.connect(expanded_meshed_region)

        @property
        def sectors_to_expand(self):
            """sectors to expand (start at 0), for multistage: use scopings container with 'stage' label."""
            return self._sectors_to_expand

        @sectors_to_expand.setter
        def sectors_to_expand(self, sectors_to_expand):
            self._sectors_to_expand.connect(sectors_to_expand)


    class _Outputs(dpf.outputs.Outputs):
        _spec = OrderedDict([(0, OutputSpec(name='cyclic_support', type_names=['cyclic_support'], document='')), (1, OutputSpec(name='sector_meshed_region', type_names=['abstract_meshed_region'], document=''))])
        def __init__(self, oper):
            self._cyclic_support = None
            self._sector_meshed_region = None
            super().__init__(self._spec, oper)

        @property
        def cyclic_support(self):
            """"""
            return self._cyclic_support

        @property
        def sector_meshed_region(self):
            """"""
            return self._sector_meshed_region


    def __init__(self, data_sources, streams_container=None, sector_meshed_region=None, expanded_meshed_region=None, sectors_to_expand=None):
        if channel is None:
            channel = dpf.server._global_channel()

        self._channel = channel
        self._stub = self._connect()
        self._message = None
        self._description = None
        self.name = "mapdl::rst::support_provider_cyclic"

        self._Operator__send_init_request()

        self.inputs = self._Inputs(self)
        self.outputs = self._Outputs(self)

    @property
    def cyclic_support(self):
        """"""
        return self.outputs._cyclic_support

    @property
    def sector_meshed_region(self):
        """"""
        return self.outputs._sector_meshed_region


