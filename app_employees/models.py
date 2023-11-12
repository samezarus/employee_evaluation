from django.db import models


class State(models.Model):
    parent = models.ForeignKey("self", verbose_name="родитель", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(verbose_name="наименование", max_length=200, default="")

    class Meta:
        ordering = ["name"]
        verbose_name = "Область"
        verbose_name_plural = "Адреса | Области"

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(
        State,
        verbose_name="область",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    parent = models.ForeignKey("self", verbose_name="родитель", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(verbose_name="наименование", max_length=200, default="")

    class Meta:
        ordering = ["name"]
        verbose_name = "Город"
        verbose_name_plural = "Адреса | Города"

    def __str__(self):
        return self.name


class Street(models.Model):
    city = models.ForeignKey(
        City,
        verbose_name="город",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    name = models.CharField(verbose_name="наименование", max_length=200, default="")
    alt_name = models.CharField(verbose_name="наименование2", max_length=200, default="")

    class Meta:
        ordering = ["name"]
        verbose_name = "Улица"
        verbose_name_plural = "Адреса | Улицы"

    def __str__(self):
        return self.name


class EmployeeGroup(models.Model):
    parent = models.ForeignKey("self", verbose_name="родитель", on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(verbose_name="наименование", max_length=200, default="")

    class Meta:
        ordering = ["name"]
        verbose_name = "Должность"
        verbose_name_plural = "Сотрудники | Должности"

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_group = models.ForeignKey(
        EmployeeGroup,
        verbose_name="должность",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    employee_group = models.ForeignKey(
        EmployeeGroup,
        verbose_name="должность",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    last_name = models.CharField(verbose_name="фамилия", max_length=100, default="")
    first_name = models.CharField(verbose_name="имя", max_length=100, default="")
    surname = models.CharField(verbose_name="отчество", max_length=100, default="")

    class Meta:
        ordering = ["last_name"]
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники | Сотрудники"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.surname}"
