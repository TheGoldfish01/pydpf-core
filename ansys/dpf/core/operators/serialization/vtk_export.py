"""
vtk_export
==========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from meshOperatorsCore plugin, from "serialization" category
"""

class vtk_export(Operator):
    """Write the input field and fields container into a given vtk path

      available inputs:
        - file_path (str)
        - mesh (MeshedRegion) (optional)
        - fields1 (FieldsContainer, Field)
        - fields2 (FieldsContainer, Field)

      available outputs:


      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.serialization.vtk_export()

      >>> # Make input connections
      >>> my_file_path = str()
      >>> op.inputs.file_path.connect(my_file_path)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_fields1 = dpf.FieldsContainer()
      >>> op.inputs.fields1.connect(my_fields1)
      >>> my_fields2 = dpf.FieldsContainer()
      >>> op.inputs.fields2.connect(my_fields2)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.serialization.vtk_export(file_path=my_file_path,mesh=my_mesh,fields1=my_fields1,fields2=my_fields2)

      >>> # Get output data"""
    def __init__(self, file_path=None, mesh=None, fields1=None, fields2=None, config=None, server=None):
        super().__init__(name="vtk_export", config = config, server = server)
        self._inputs = InputsVtkExport(self)
        self._outputs = OutputsVtkExport(self)
        if file_path !=None:
            self.inputs.file_path.connect(file_path)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)
        if fields1 !=None:
            self.inputs.fields1.connect(fields1)
        if fields2 !=None:
            self.inputs.fields2.connect(fields2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Write the input field and fields container into a given vtk path""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "file_path", type_names=["string"], optional=False, document="""path with vtk extension were the export occurs"""), 
                                 1 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=True, document="""necessary if the first field or fields container don't have a mesh in their support"""), 
                                 2 : PinSpecification(name = "fields", type_names=["fields_container","field"], optional=False, document="""fields exported"""), 
                                 3 : PinSpecification(name = "fields", type_names=["fields_container","field"], optional=False, document="""fields exported""")},
                             map_output_pin_spec={
})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "vtk_export")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsVtkExport 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsVtkExport 
        """
        return super().outputs


#internal name: vtk_export
#scripting name: vtk_export
class InputsVtkExport(_Inputs):
    """Intermediate class used to connect user inputs to vtk_export operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.vtk_export()
      >>> my_file_path = str()
      >>> op.inputs.file_path.connect(my_file_path)
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
      >>> my_fields1 = dpf.FieldsContainer()
      >>> op.inputs.fields1.connect(my_fields1)
      >>> my_fields2 = dpf.FieldsContainer()
      >>> op.inputs.fields2.connect(my_fields2)
    """
    def __init__(self, op: Operator):
        super().__init__(vtk_export._spec().inputs, op)
        self._file_path = Input(vtk_export._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._file_path)
        self._mesh = Input(vtk_export._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._mesh)
        self._fields1 = Input(vtk_export._spec().input_pin(2), 2, op, 0) 
        self._inputs.append(self._fields1)
        self._fields2 = Input(vtk_export._spec().input_pin(3), 3, op, 1) 
        self._inputs.append(self._fields2)

    @property
    def file_path(self):
        """Allows to connect file_path input to the operator

        - pindoc: path with vtk extension were the export occurs

        Parameters
        ----------
        my_file_path : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.vtk_export()
        >>> op.inputs.file_path.connect(my_file_path)
        >>> #or
        >>> op.inputs.file_path(my_file_path)

        """
        return self._file_path

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        - pindoc: necessary if the first field or fields container don't have a mesh in their support

        Parameters
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.vtk_export()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

    @property
    def fields1(self):
        """Allows to connect fields1 input to the operator

        - pindoc: fields exported

        Parameters
        ----------
        my_fields1 : FieldsContainer, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.vtk_export()
        >>> op.inputs.fields1.connect(my_fields1)
        >>> #or
        >>> op.inputs.fields1(my_fields1)

        """
        return self._fields1

    @property
    def fields2(self):
        """Allows to connect fields2 input to the operator

        - pindoc: fields exported

        Parameters
        ----------
        my_fields2 : FieldsContainer, Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.serialization.vtk_export()
        >>> op.inputs.fields2.connect(my_fields2)
        >>> #or
        >>> op.inputs.fields2(my_fields2)

        """
        return self._fields2

class OutputsVtkExport(_Outputs):
    """Intermediate class used to get outputs from vtk_export operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.serialization.vtk_export()
      >>> # Connect inputs : op.inputs. ...
    """
    def __init__(self, op: Operator):
        super().__init__(vtk_export._spec().outputs, op)
        pass 

