"""
node_coordinates
================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "mesh" category
"""

class node_coordinates(Operator):
    """Returns the node coordinates of the mesh(es) in input

      available inputs:
        - mesh (MeshedRegion, MeshesContainer)

      available outputs:
        - coordinates (Field ,FieldsContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.node_coordinates()

      >>> # Make input connections
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.node_coordinates(mesh=my_mesh)

      >>> # Get output data
      >>> result_coordinates = op.outputs.coordinates()"""
    def __init__(self, mesh=None, config=None, server=None):
        super().__init__(name="mesh::node_coordinates", config = config, server = server)
        self._inputs = InputsNodeCoordinates(self)
        self._outputs = OutputsNodeCoordinates(self)
        if mesh !=None:
            self.inputs.mesh.connect(mesh)

    @staticmethod
    def _spec():
        spec = Specification(description="""Returns the node coordinates of the mesh(es) in input""",
                             map_input_pin_spec={
                                 7 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region","meshes_container"], optional=False, document="""""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "coordinates", type_names=["field","fields_container"], optional=False, document="""if the input is a meshed region, a field of coordinates is the output, else if the input is a  meshes container, a fields container (one field by mesh) is the output""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mesh::node_coordinates")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsNodeCoordinates 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsNodeCoordinates 
        """
        return super().outputs


#internal name: mesh::node_coordinates
#scripting name: node_coordinates
class InputsNodeCoordinates(_Inputs):
    """Intermediate class used to connect user inputs to node_coordinates operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.node_coordinates()
      >>> my_mesh = dpf.MeshedRegion()
      >>> op.inputs.mesh.connect(my_mesh)
    """
    def __init__(self, op: Operator):
        super().__init__(node_coordinates._spec().inputs, op)
        self._mesh = Input(node_coordinates._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._mesh)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator

        Parameters
        ----------
        my_mesh : MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.node_coordinates()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> #or
        >>> op.inputs.mesh(my_mesh)

        """
        return self._mesh

class OutputsNodeCoordinates(_Outputs):
    """Intermediate class used to get outputs from node_coordinates operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.node_coordinates()
      >>> # Connect inputs : op.inputs. ...
      >>> result_coordinates = op.outputs.coordinates()
    """
    def __init__(self, op: Operator):
        super().__init__(node_coordinates._spec().outputs, op)
        self.coordinates_as_field = Output( _modify_output_spec_with_one_type(node_coordinates._spec().output_pin(0), "field"), 0, op) 
        self._outputs.append(self.coordinates_as_field)
        self.coordinates_as_fields_container = Output( _modify_output_spec_with_one_type(node_coordinates._spec().output_pin(0), "fields_container"), 0, op) 
        self._outputs.append(self.coordinates_as_fields_container)
