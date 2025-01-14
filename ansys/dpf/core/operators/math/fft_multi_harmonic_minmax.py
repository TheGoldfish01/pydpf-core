"""
fft_multi_harmonic_minmax
=========================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Math plugin, from "math" category
"""

class fft_multi_harmonic_minmax(Operator):
    """Evaluate min max fields on multi harmonic solution. min and max fields are calculated based on evaluating a fft wrt rpms and using the gradient method for adaptive time steping

      available inputs:
        - fields_container (FieldsContainer)
        - rpm_scoping (Scoping) (optional)
        - fs_ratio (int) (optional)
        - num_subdivisions (int) (optional)
        - max_num_subdivisions (int) (optional)

      available outputs:
        - field_min (FieldsContainer)
        - field_max (FieldsContainer)
        - all_fields (FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.math.fft_multi_harmonic_minmax()

      >>> # Make input connections
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_rpm_scoping = dpf.Scoping()
      >>> op.inputs.rpm_scoping.connect(my_rpm_scoping)
      >>> my_fs_ratio = int()
      >>> op.inputs.fs_ratio.connect(my_fs_ratio)
      >>> my_num_subdivisions = int()
      >>> op.inputs.num_subdivisions.connect(my_num_subdivisions)
      >>> my_max_num_subdivisions = int()
      >>> op.inputs.max_num_subdivisions.connect(my_max_num_subdivisions)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.math.fft_multi_harmonic_minmax(fields_container=my_fields_container,rpm_scoping=my_rpm_scoping,fs_ratio=my_fs_ratio,num_subdivisions=my_num_subdivisions,max_num_subdivisions=my_max_num_subdivisions)

      >>> # Get output data
      >>> result_field_min = op.outputs.field_min()
      >>> result_field_max = op.outputs.field_max()
      >>> result_all_fields = op.outputs.all_fields()"""
    def __init__(self, fields_container=None, rpm_scoping=None, fs_ratio=None, num_subdivisions=None, max_num_subdivisions=None, config=None, server=None):
        super().__init__(name="fft_multi_harmonic_minmax", config = config, server = server)
        self._inputs = InputsFftMultiHarmonicMinmax(self)
        self._outputs = OutputsFftMultiHarmonicMinmax(self)
        if fields_container !=None:
            self.inputs.fields_container.connect(fields_container)
        if rpm_scoping !=None:
            self.inputs.rpm_scoping.connect(rpm_scoping)
        if fs_ratio !=None:
            self.inputs.fs_ratio.connect(fs_ratio)
        if num_subdivisions !=None:
            self.inputs.num_subdivisions.connect(num_subdivisions)
        if max_num_subdivisions !=None:
            self.inputs.max_num_subdivisions.connect(max_num_subdivisions)

    @staticmethod
    def _spec():
        spec = Specification(description="""Evaluate min max fields on multi harmonic solution. min and max fields are calculated based on evaluating a fft wrt rpms and using the gradient method for adaptive time steping""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fields_container", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "rpm_scoping", type_names=["scoping"], optional=True, document="""rpm scoping, by default the fft is evaluted using all the rpms"""), 
                                 2 : PinSpecification(name = "fs_ratio", type_names=["int32"], optional=True, document="""field or fields container with only one field is expected"""), 
                                 3 : PinSpecification(name = "num_subdivisions", type_names=["int32"], optional=True, document="""connect number subdivisions, used for uniform discretization"""), 
                                 4 : PinSpecification(name = "max_num_subdivisions", type_names=["int32"], optional=True, document="""connect max number subdivisions, used to avoid huge number of sudivisions""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "field_min", type_names=["fields_container"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "field_max", type_names=["fields_container"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "all_fields", type_names=["fields_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "fft_multi_harmonic_minmax")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsFftMultiHarmonicMinmax 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsFftMultiHarmonicMinmax 
        """
        return super().outputs


#internal name: fft_multi_harmonic_minmax
#scripting name: fft_multi_harmonic_minmax
class InputsFftMultiHarmonicMinmax(_Inputs):
    """Intermediate class used to connect user inputs to fft_multi_harmonic_minmax operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
      >>> my_fields_container = dpf.FieldsContainer()
      >>> op.inputs.fields_container.connect(my_fields_container)
      >>> my_rpm_scoping = dpf.Scoping()
      >>> op.inputs.rpm_scoping.connect(my_rpm_scoping)
      >>> my_fs_ratio = int()
      >>> op.inputs.fs_ratio.connect(my_fs_ratio)
      >>> my_num_subdivisions = int()
      >>> op.inputs.num_subdivisions.connect(my_num_subdivisions)
      >>> my_max_num_subdivisions = int()
      >>> op.inputs.max_num_subdivisions.connect(my_max_num_subdivisions)
    """
    def __init__(self, op: Operator):
        super().__init__(fft_multi_harmonic_minmax._spec().inputs, op)
        self._fields_container = Input(fft_multi_harmonic_minmax._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fields_container)
        self._rpm_scoping = Input(fft_multi_harmonic_minmax._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._rpm_scoping)
        self._fs_ratio = Input(fft_multi_harmonic_minmax._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._fs_ratio)
        self._num_subdivisions = Input(fft_multi_harmonic_minmax._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._num_subdivisions)
        self._max_num_subdivisions = Input(fft_multi_harmonic_minmax._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._max_num_subdivisions)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator

        Parameters
        ----------
        my_fields_container : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> #or
        >>> op.inputs.fields_container(my_fields_container)

        """
        return self._fields_container

    @property
    def rpm_scoping(self):
        """Allows to connect rpm_scoping input to the operator

        - pindoc: rpm scoping, by default the fft is evaluted using all the rpms

        Parameters
        ----------
        my_rpm_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> op.inputs.rpm_scoping.connect(my_rpm_scoping)
        >>> #or
        >>> op.inputs.rpm_scoping(my_rpm_scoping)

        """
        return self._rpm_scoping

    @property
    def fs_ratio(self):
        """Allows to connect fs_ratio input to the operator

        - pindoc: field or fields container with only one field is expected

        Parameters
        ----------
        my_fs_ratio : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> op.inputs.fs_ratio.connect(my_fs_ratio)
        >>> #or
        >>> op.inputs.fs_ratio(my_fs_ratio)

        """
        return self._fs_ratio

    @property
    def num_subdivisions(self):
        """Allows to connect num_subdivisions input to the operator

        - pindoc: connect number subdivisions, used for uniform discretization

        Parameters
        ----------
        my_num_subdivisions : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> op.inputs.num_subdivisions.connect(my_num_subdivisions)
        >>> #or
        >>> op.inputs.num_subdivisions(my_num_subdivisions)

        """
        return self._num_subdivisions

    @property
    def max_num_subdivisions(self):
        """Allows to connect max_num_subdivisions input to the operator

        - pindoc: connect max number subdivisions, used to avoid huge number of sudivisions

        Parameters
        ----------
        my_max_num_subdivisions : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> op.inputs.max_num_subdivisions.connect(my_max_num_subdivisions)
        >>> #or
        >>> op.inputs.max_num_subdivisions(my_max_num_subdivisions)

        """
        return self._max_num_subdivisions

class OutputsFftMultiHarmonicMinmax(_Outputs):
    """Intermediate class used to get outputs from fft_multi_harmonic_minmax operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
      >>> # Connect inputs : op.inputs. ...
      >>> result_field_min = op.outputs.field_min()
      >>> result_field_max = op.outputs.field_max()
      >>> result_all_fields = op.outputs.all_fields()
    """
    def __init__(self, op: Operator):
        super().__init__(fft_multi_harmonic_minmax._spec().outputs, op)
        self._field_min = Output(fft_multi_harmonic_minmax._spec().output_pin(0), 0, op) 
        self._outputs.append(self._field_min)
        self._field_max = Output(fft_multi_harmonic_minmax._spec().output_pin(1), 1, op) 
        self._outputs.append(self._field_max)
        self._all_fields = Output(fft_multi_harmonic_minmax._spec().output_pin(2), 2, op) 
        self._outputs.append(self._all_fields)

    @property
    def field_min(self):
        """Allows to get field_min output of the operator


        Returns
        ----------
        my_field_min : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_min = op.outputs.field_min() 
        """
        return self._field_min

    @property
    def field_max(self):
        """Allows to get field_max output of the operator


        Returns
        ----------
        my_field_max : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_max = op.outputs.field_max() 
        """
        return self._field_max

    @property
    def all_fields(self):
        """Allows to get all_fields output of the operator


        Returns
        ----------
        my_all_fields : FieldsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.math.fft_multi_harmonic_minmax()
        >>> # Connect inputs : op.inputs. ...
        >>> result_all_fields = op.outputs.all_fields() 
        """
        return self._all_fields

