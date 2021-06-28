from enum import Enum


class OsArchitectures(Enum):
    """
    An enumeration which defines the in Cobbler available architectures.
    """
    i386 = 1
    """
    32-bit architecture which is also called ``IA-32`` or ``80x86`` by some people.
    """
    x86_64 = 2
    """
    64-bit architecture which is also called ``x64``, ``x86-64``, ``AMD64`` or ``amd64``.
    """
    ppc = 3
    """
    32-bit big-endian PowerPC architecture.
    """
    ppc64 = 4
    """
    64-bit big-endian PowerPC architecture.
    """
    amd64 = 5
    """
    Synonym for ``x86_64``.
    """


class RepositoryBreeds(Enum):
    """
    An enumeration which defines the in Cobbler available repository breeds.
    """
    rsync = 1
    """
    A repository which is synced by rsync.
    """
    rhn = 2
    """
    A repository type from Red Hat which can be used by yum.
    """
    yum = 3
    """
    A repository which is manged by yum.
    """
    apt = 4
    """
    A repository which is managed by apt.
    """


class Osversion:
    """
    A version of an operating system breed like ``openSUSE Leap 15.2``. The specification of the attributes and what
    values are valid are described in the JSON specification.
    """

    def __init__(self):
        """
        Creates default values for all values.
        """
        self._signatures = []
        self._version_file = ""
        self._version_file_regex = ""
        self._kernel_arch = ""
        self._kernel_arch_regex = ""
        self._supported_arches = []
        self._supported_repo_breeds = []
        self._kernel_file = ""
        self._initrd_file = ""
        self._isolinux_ok = False
        self._default_autoinstall = ""
        self._kernel_options = ""
        self._kernel_options_post = ""
        self._template_files = ""
        self._boot_files = []
        self._boot_loaders = {}

    def __eq__(self, other) -> bool:
        """
        Checks for equality. Equality is given if all attributes are identical.

        :param other: The other object.
        :raises NotImplemented: In case other is not Osversion
        :return: Only true if all attributes are identical.
        """
        if not isinstance(other, Osversion):
            return NotImplemented
        return self.signatures == other.signatures \
            and self.version_file == other.version_file \
            and self.version_file_regex == other.version_file_regex \
            and self.kernel_arch == other.kernel_arch \
            and self.kernel_arch_regex == other.kernel_arch_regex \
            and self.supported_arches == other.supported_arches \
            and self.supported_repo_breeds == other.supported_repo_breeds \
            and self.kernel_file == other.kernel_file \
            and self.initrd_file == other.initrd_file \
            and self.isolinux_ok == other.isolinux_ok \
            and self.default_autoinstall == other.default_autoinstall \
            and self.kernel_options == other.kernel_options \
            and self.kernel_options_post == other.kernel_options_post \
            and self.template_files == other._template_files \
            and self.boot_files == other.boot_files \
            and self.boot_loaders == other.boot_loaders

    @property
    def signatures(self) -> list:
        """
        This is a list of strings with currently an unknown functionality.

        :setter: May raise a TypeError in case the value was not of type list.
        :getter: Returns the last correctly validated str of the property.
        :deleter: Resets this to an empty list.
        :type: list
        """
        return self._signatures

    @signatures.setter
    def signatures(self, value: list):
        """
        Setter for the signatures.

        :param value: The list with the signatures.
        :raises TypeError: In case the value was not of of type list.
        """
        if isinstance(value, list):
            self._signatures = value
        else:
            raise TypeError("Signatures should be a list.")

    @signatures.deleter
    def signatures(self):
        """
        Resets the value of the signatures to an emtpy list.
        """
        self._signatures = []

    @property
    def version_file(self) -> str:
        """
        The regular expression which points to the file with the os-version info.

        :setter: May raise a TypeError in case the value was not of type str.
        :getter: Returns the last correctly validated str of the property.
        :deleter: Resets this to an empty string.
        :type: str
        """
        return self._version_file

    @version_file.setter
    def version_file(self, value: str):
        """
        Setter for the version_file.

        :param value: The string which will become the version file.
        :raises TypeError: In case the value is not a str.
        """
        if isinstance(value, str):
            self._version_file = value
        else:
            raise TypeError("The version_file should be a str.")

    @version_file.deleter
    def version_file(self):
        """
        Resets the version_file to an empty string instead of deleting the attribute.
        """
        self._version_file = ""

    @property
    def version_file_regex(self) -> str:
        """
        The regular expression which tells Cobbler to pick this version if it matches.

        :getter: The str with the regex.
        :setter: Validates the regex and raises in case an error was detected (TypeError).
        :deleter: Resets the attribute to an empty str instead of deleting it.
        :type: str
        """
        return self._version_file_regex

    @version_file_regex.setter
    def version_file_regex(self, value: str):
        """
        Setter for the version_file_regex.

        :param value: The str with the new value.
        :raises TypeError: In case the regex was not of type str.
        """
        if isinstance(value, str):
            # TODO validate regex - regex syntax
            self._version_file_regex = value
        else:
            raise TypeError("The version_file_regex should be a str.")

    @version_file_regex.deleter
    def version_file_regex(self):
        """
        Resets the version_file_regex to an empty string instead of deleting the attribute.
        """
        self._version_file_regex = ""

    @property
    def kernel_arch(self) -> str:
        """
        The regular expression which tells Cobbler where to look for the architecture of the operating system.
        In some cases this may also be a path to the file where Cobbler should look for the architecture.

        :getter: The value of the last successfully validated kernel_arch.
        :setter: May raise a TypeError in case the value was not of type str.
        :deleter: Resets the value instead of deleting the attribute.
        :type: str
        """
        return self._kernel_arch

    @kernel_arch.setter
    def kernel_arch(self, value: str):
        """
        Setter for the kernel_arch.

        :param value: The new str for the kernel_arch.
        :raises TypeError: In case ``value`` was not of type str.
        """
        if isinstance(value, str):
            self._kernel_arch = value
        else:
            raise TypeError("The kernel_arch should be a str.")

    @kernel_arch.deleter
    def kernel_arch(self):
        """
        Resets the kernel_arch to an empty string instead of deleting the attribute.
        """
        self._kernel_arch = ""

    @property
    def kernel_arch_regex(self) -> str:
        """
        In case ``kernel_arch`` does not point to the architecture directly, this is the regex where Cobbler looks for
        in the file specified by ``kernel_arch``.

        :getter: The last successfully validated value of this field.
        :setter: Will set this if the validation succeeds, otherwise will raise an exception (TypeError).
        :deleter: Resets this to an empty str.
        :type: str
        """
        return self._kernel_arch_regex

    @kernel_arch_regex.setter
    def kernel_arch_regex(self, value: str):
        """
        Setter for the kernel_arch_regex.

        :param value: The new str for the ``kernel_arch_regex``.
        :raises TypeError: In case value was not of type str.
        """
        if isinstance(value, str):
            # TODO validate regex - regex syntax
            self._kernel_arch_regex = value
        else:
            raise TypeError("The kernel_arch_regex should be a str.")

    @kernel_arch_regex.deleter
    def kernel_arch_regex(self):
        """
        Resets the kernel_arch_regex to an empty string instead of deleting the attribute.
        """
        self._kernel_arch_regex = ""

    @property
    def supported_arches(self) -> list:
        """
        Unused field currently. There for compatibility reasons for now.

        :getter: The last successfully validated value of this field.
        :setter: Will set this if the validation succeeds, otherwise will raise an exception (TypeError).
        :deleter: Resets this to an empty list.
        :type: list
        """
        return self._supported_arches

    @supported_arches.setter
    def supported_arches(self, value: list):
        """
        Setter for the supported_arches.

        :param value: The new list for the ``supported_arches``.
        :raises TypeError: In case value is not of type list.
        """
        if isinstance(value, list):
            self._supported_arches = value
        else:
            raise TypeError("The supported_arches should be a list.")

    @supported_arches.deleter
    def supported_arches(self):
        """
        Resets the supported_arches to an empty list instead of deleting the attribute.
        """
        self._supported_arches = []

    @property
    def supported_repo_breeds(self) -> list:
        """
        Unused field currently. There for compatibility reasons for now.

        :getter: The last successfully validated value of this field.
        :setter: Will set this if the validation succeeds, otherwise will raise an exception (TypeError).
        :deleter: Resets this to an empty list.
        :type: list
        """
        return self._supported_repo_breeds

    @supported_repo_breeds.setter
    def supported_repo_breeds(self, value: list):
        """
        Setter for supported_repo_breeds.

        :param value: The new list for the ``supported_repo_breeds``.
        :raises TypeError: In case value is not of type list.
        """
        if isinstance(value, list):
            self._supported_repo_breeds = value
        else:
            raise TypeError("The supported_repo_breeds should be a list.")

    @supported_repo_breeds.deleter
    def supported_repo_breeds(self):
        """
        Resets the supported_repo_breeds to an empty list instead of deleting the attribute.
        """
        self._supported_repo_breeds = []

    @property
    def kernel_file(self) -> str:
        """
        The regular expression to match to find the kernel.

        :getter: The last successfully validated value of this field.
        :setter: Will set this if the validation succeeds, otherwise will raise an exception (TypeError).
        :deleter: Resets this to an empty str.
        :type: str
        """
        return self._kernel_file

    @kernel_file.setter
    def kernel_file(self, value: str):
        """
        Setter for the kernel_file.

        :param value: The new str for the ``kernel_file``.
        :raises TypeError: In case value is not of type str.
        """
        if isinstance(value, str):
            self._kernel_file = value
        else:
            raise TypeError("The kernel_file should be a str.")

    @kernel_file.deleter
    def kernel_file(self):
        """
        Resets the kernel_file to an empty string instead of deleting the attribute.
        """
        self._kernel_file = ""

    @property
    def initrd_file(self) -> str:
        """
        The regular expression to match to find the initrd.

        :getter: The last successfully validated value of this field.
        :setter: Will set this if the validation succeeds, otherwise will raise an exception (TypeError).
        :deleter: Resets this to an empty str.
        :type: str
        """
        return self._initrd_file

    @initrd_file.setter
    def initrd_file(self, value: str):
        """
        Setter for the initrd_file.

        :param value: The new str for the ``initrd_file``.
        :raises TypeError: In case value is not of type str.
        """
        if isinstance(value, str):
            self._initrd_file = value
        else:
            raise TypeError("The initrd_file should be a str.")

    @initrd_file.deleter
    def initrd_file(self):
        """
        Resets the initrd_file to an empty string instead of deleting the attribute.
        """
        self._initrd_file = ""

    @property
    def isolinux_ok(self) -> bool:
        """
        Unknown field currently. There for compatibility reasons for now.

        :getter: The last successfully validated value of this field.
        :setter: Will set this if the validation succeeds, otherwise will raise an exception (TypeError).
        :deleter: Resets this to ``False``.
        :type: bool
        """
        return self._isolinux_ok

    @isolinux_ok.setter
    def isolinux_ok(self, value: bool):
        """
        Setter for isolinux_ok.

        :param value: The new bool for ``isolinux_ok``.
        :raises TypeError: In case value is not of type bool.
        """
        if isinstance(value, bool):
            self._isolinux_ok = value
        else:
            raise TypeError("The isolinux_ok should be a bool.")

    @isolinux_ok.deleter
    def isolinux_ok(self):
        """
        Resets the isolinux_ok to ``False`` instead of deleting the attribute.
        """
        self._isolinux_ok = False

    @property
    def default_autoinstall(self) -> str:
        """
        The filename for the default autoinstall template in Cobbler.

        :getter: The last successfully validated value of this field.
        :setter: Will set this if the validation succeeds, otherwise will raise an exception (TypeError).
        :deleter: Resets this to an empty str.
        :type: str
        """
        return self._default_autoinstall

    @default_autoinstall.setter
    def default_autoinstall(self, value: str):
        """
        Setter for default_autoinstall.

        :param value: The new str for the ``default_autoinstall``.
        :raises TypeError: In case value is not of type str.
        """
        if isinstance(value, str):
            self._default_autoinstall = value
        else:
            raise TypeError("The default_autoinstall should be a str.")

    @default_autoinstall.deleter
    def default_autoinstall(self):
        """
        Resets the default_autoinstall to an empty string instead of deleting the attribute.
        """
        self._default_autoinstall = ""

    @property
    def kernel_options(self) -> str:
        """
        Default kernel options to apply to the imported ISO.

        :getter: The last successfully validated value of this field.
        :setter: Will set this if the validation succeeds, otherwise will raise an exception (TypeError).
        :deleter: Resets this to an empty str.
        :type: str
        """
        return self._kernel_options

    @kernel_options.setter
    def kernel_options(self, value: str):
        """
        Setter for kernel_options.

        :param value: The new str for the ``kernel_options``.
        :raises TypeError: In case value is not of type str.
        """
        if isinstance(value, str):
            self._kernel_options = value
        else:
            raise TypeError("The kernel_options should be a str.")

    @kernel_options.deleter
    def kernel_options(self):
        """
        Resets the kernel_options to an empty string instead of deleting the attribute.
        """
        self._kernel_options = ""

    @property
    def kernel_options_post(self) -> str:
        """
        Default kernel post options to apply to the imported ISO.

        :getter: The last successfully validated value of this field.
        :setter: Will set this if the validation succeeds, otherwise will raise an exception (TypeError).
        :deleter: Resets this to an empty str.
        :type: str
        """
        return self._kernel_options_post

    @kernel_options_post.setter
    def kernel_options_post(self, value: str):
        """
        Setter for kernel_options_post

        :param value: The new str for the ``kernel_options_post``.
        :raises TypeError: In case value is not of type str.
        """
        if isinstance(value, str):
            self._kernel_options_post = value
        else:
            raise TypeError("The kernel_options_post should be a str.")

    @kernel_options_post.deleter
    def kernel_options_post(self):
        """
        Resets the kernel_options_post to an empty string instead of deleting the attribute.
        """
        self._kernel_options_post = ""

    @property
    def template_files(self) -> str:
        """
        Currently only used in ESXi. Needs more investigation what this is for.

        :getter: The last successfully validated value of this field.
        :setter: Will set this if the validation succeeds, otherwise will raise an exception (TypeError).
        :deleter: Resets this to an empty str.
        :type: str
        """
        return self._template_files

    @template_files.setter
    def template_files(self, value: str):
        """
        Setter for template_files.

        :param value: The new str for the ``template_files``.
        :raises TypeError: In case value is not of type str.
        """
        if isinstance(value, str):
            # TODO validate file path
            self._template_files = value
        else:
            raise TypeError("The template_files should be a str.")

    @template_files.deleter
    def template_files(self):
        """
        Resets the template_files to an empty string instead of deleting the attribute.
        """
        self._template_files = ""

    @property
    def boot_files(self) -> list:
        """
        Unknown field currently. There for compatibility reasons for now. Used by xenserver

        :getter: The last successfully validated value of this field.
        :setter: Will set this if the validation succeeds, otherwise will raise an exception (TypeError).
        :deleter: Resets this to an empty list.
        :type: list
        """
        return self._boot_files

    @boot_files.setter
    def boot_files(self, value: list):
        """
        Setter for the ``boot_files``.

        :param value: The new boot files which should be set.
        :raises TypeError: In case value was not of type list.
        """
        if isinstance(value, list):
            self._boot_files = value
        else:
            raise TypeError("The boot_files should be a list.")

    @boot_files.deleter
    def boot_files(self):
        """
        Resets the boot_files to an empty list instead of deleting the attribute.
        """
        self._boot_files = []

    @property
    def boot_loaders(self) -> dict:
        """
        Defines the supported well known boot loaders inside Cobbler.

        :getter: The last successfully validated value of this field.
        :setter: If validation is successful the value will be set, otherwise raises an exception (TypeError).
        :deleter: Resets this property to an empty dict.
        :type: dict
        """
        return self._boot_loaders

    @boot_loaders.setter
    def boot_loaders(self, value: dict):
        """
        Setter for the ``boot_loaders``.

        :param value: The new boot loaders which should be set.
        :raises TypeError: In case value was not of type dict.
        """
        if isinstance(value, dict):
            # TODO validate dict format
            self._boot_loaders = value
        else:
            raise TypeError("The boot_loaders should be a dict.")

    @boot_loaders.deleter
    def boot_loaders(self):
        """
        Resets the boot_loaders to an empty dictionary instead of deleting the attribute.
        """
        self._boot_loaders = {}

    def encode(self) -> dict:
        """
        Encodes a single :class:`Osversion`. This means that the properties of an object is transferred into a JSON.

        :return: The dictionary with the data.
        """
        return {
            "signatures": self.signatures,
            "version_file": self.version_file,
            "version_file_regex": self.version_file_regex,
            "kernel_arch": self.kernel_arch,
            "kernel_arch_regex": self.kernel_arch_regex,
            "supported_arches": self.supported_arches,
            "supported_repo_breeds": self.supported_repo_breeds,
            "kernel_file": self.kernel_file,
            "initrd_file": self.initrd_file,
            "isolinux_ok": self.isolinux_ok,
            "default_autoinstall": self.default_autoinstall,
            "kernel_options": self.kernel_options,
            "kernel_options_post": self.kernel_options_post,
            "template_files": self._template_files,
            "boot_files": self.boot_files,
            "boot_loaders": self.boot_loaders
        }

    def decode(self, data):
        """
        Decodes the received data. This means parsing each attribute from the JSON into the property of an object.

        :param data: The data to decode.
        """
        self.signatures = data.get("signatures", [])
        self.version_file = data.get("version_file", "")
        self.version_file_regex = data.get("version_file_regex", "")
        self.kernel_arch = data.get("kernel_arch", "")
        self.kernel_arch_regex = data.get("kernel_arch_regex", "")
        self.supported_arches = data.get("supported_arches", [])
        self.supported_repo_breeds = data.get("supported_repo_breeds", [])
        self.kernel_file = data.get("kernel_file", [])
        self.initrd_file = data.get("initrd_file", "")
        self.isolinux_ok = data.get("isolinux_ok", False)
        self.default_autoinstall = data.get("default_autoinstall", "")
        self.kernel_options = data.get("kernel_options", "")
        self.kernel_options_post = data.get("kernel_options_post", "")
        self.template_files = data.get("template_files", "")
        self.boot_files = data.get("boot_files", [])
        self.boot_loaders = data.get("boot_loaders", {})
